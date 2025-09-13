from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from openai import OpenAI
import json
from pathlib import Path
from ..config import QDRANT_HOST, QDRANT_PORT, COLLECTION_NAME, OPENAI_API_KEY

class MovieService:
    def __init__(self):
        self.client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
        self.openai_client = OpenAI(api_key=OPENAI_API_KEY)
        self.setup_collection()

    def setup_collection(self):
        collections = self.client.get_collections().collections
        collection_exists = any(c.name == COLLECTION_NAME for c in collections)

        if not collection_exists:
            print(f"Creating new collection: {COLLECTION_NAME}")
            self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
            )
            # Load initial data only when collection is first created
            self._load_initial_data()
        else:
            # Check if existing collection is empty
            collection_info = self.client.get_collection(COLLECTION_NAME)
            if collection_info.points_count == 0:
                print(f"Collection {COLLECTION_NAME} exists but is empty, loading initial data...")
                self._load_initial_data()
            else:
                print(f"Collection {COLLECTION_NAME} already has {collection_info.points_count} movies, skipping data load")

    def _load_initial_data(self):
        """Load initial movie data from JSON file when collection is empty"""
        try:
            data_path = Path(__file__).parent.parent.parent / "data" / "movies.json"
            
            if data_path.exists():
                with open(data_path, 'r', encoding='utf-8') as f:
                    movies = json.load(f)
                
                print(f"Loading {len(movies)} movies into collection...")
                
                # Process movies in batches for better performance
                batch_size = 10
                points = []
                
                for i, movie in enumerate(movies):
                    text = f"{movie['title']} {movie['genre']} {movie['director']} {movie['description']}"
                    vector = self.get_embedding(text)
                    point = PointStruct(
                        id=movie["id"], 
                        vector=vector, 
                        payload=movie
                    )
                    points.append(point)
                    
                    # Upsert in batches
                    if len(points) >= batch_size or i == len(movies) - 1:
                        self.client.upsert(collection_name=COLLECTION_NAME, points=points)
                        print(f"Loaded {min(i + 1, len(movies))}/{len(movies)} movies")
                        points = []
                
                print("Initial data loading completed!")
            else:
                print(f"Data file not found at {data_path}")
                
        except Exception as e:
            print(f"Error loading initial data: {e}")

    def get_embedding(self, text: str):
        """Get OpenAI text-embedding-ada-002 embedding for text"""
        response = self.openai_client.embeddings.create(
            model="text-embedding-ada-002", input=text
        )
        return response.data[0].embedding

    def add_movie(self, movie_data: dict):
        """Add a single movie to the collection"""
        text = f"{movie_data['title']} {movie_data['genre']} {movie_data['director']} {movie_data['description']}"
        vector = self.get_embedding(text)

        point = PointStruct(id=movie_data["id"], vector=vector, payload=movie_data)

        self.client.upsert(collection_name=COLLECTION_NAME, points=[point])

    def search_movies(self, query: str, limit: int = 5):
        query_vector = self.get_embedding(query)

        results = self.client.search(
            collection_name=COLLECTION_NAME, query_vector=query_vector, limit=limit
        )

        return results