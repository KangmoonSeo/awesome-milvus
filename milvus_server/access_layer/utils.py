# access_layer/utils.py
from typing import List
import numpy as np

def calculate_cosine_similarity(query_vector: List[float], vectors: List[List[float]]):
    query = np.array(query_vector)
    similarities = [
        np.dot(query, np.array(vec)) / (np.linalg.norm(query) * np.linalg.norm(vec)) 
        for vec in vectors
    ]
    return similarities

def get_top_k_indices(similarities, top_k):
    return np.argsort(similarities)[-top_k:][::-1]
