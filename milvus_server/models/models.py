# access_layer/models.py
from pydantic import BaseModel
from typing import List


class Collection(BaseModel):
    name: str
    description: str


class QueryRequest(BaseModel):
    collection: str
    vector: List[float]
    top_k: int
