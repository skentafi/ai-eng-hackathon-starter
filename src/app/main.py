from fastapi import FastAPI, HTTPException
from .schemas import Movie, SearchResponse, MovieResponse
from .services import MovieService
import json
from pathlib import Path

app = FastAPI(title="Movie Recommender", version="0.1.0")
movie_service = MovieService()


@app.on_event("startup")
async def startup_event():
    print("Movie service initialized")


@app.post("/movies", response_model=dict)
async def add_movie(movie: Movie):
    try:
        movie_service.add_movie(movie.dict())
        return {"message": f"Movie '{movie.title}' added successfully", "id": movie.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search", response_model=SearchResponse)
async def search_movies(q: str, limit: int = 5):
    try:
        results = movie_service.search_movies(q, limit)

        movie_responses = []
        for result in results:
            movie_data = Movie(**result.payload)
            movie_response = MovieResponse(movie=movie_data, score=result.score)
            movie_responses.append(movie_response)

        return SearchResponse(query=q, results=movie_responses)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))