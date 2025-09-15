from pydantic import BaseModel
from typing import List, Optional


class Movie(BaseModel):
    id: int
    title: str
    genre: str
    director: str
    year: int
    rating: float
    description: str


class MovieResponse(BaseModel):
    movie: Movie
    score: float


class SearchResponse(BaseModel):
    query: str
    results: List[MovieResponse]
