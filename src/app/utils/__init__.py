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
            self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
            )

    def get_embedding(self, text: str):
        """Get OpenAI text-embedding-ada-002 embedding for text"""
        response = self.openai_client.embeddings.create(
            model="text-embedding-ada-002", input=text
        )
        return response.data[0].embedding

    def add_movie(self, movie_data: dict):
        # Create text for embedding
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
