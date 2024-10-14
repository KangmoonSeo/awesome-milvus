# worker_nodes/query_node.py
from fastapi import FastAPI, HTTPException
import numpy as np

from models.models import QueryRequest
from worker_nodes.core.vector_db import load_vector_db

app = FastAPI()


@app.post("/query_node/search")
def search(query_request: QueryRequest):
    collection_name = query_request.collection
    vector_db = load_vector_db()

    if collection_name not in vector_db:
        raise HTTPException(status_code=404, detail="Collection not found")

    query_vector = np.array(query_request.vector)
    top_k = query_request.top_k
    collection_vectors = vector_db[collection_name]

    # Perform a basic cosine similarity search
    similarities = [
        np.dot(query_vector, vec) / (np.linalg.norm(query_vector) * np.linalg.norm(vec))
        for vec in collection_vectors
    ]
    top_k_indices = np.argsort(similarities)[-top_k:][::-1]
    results = [
        {"vector": collection_vectors[i].tolist(), "similarity": similarities[i]}
        for i in top_k_indices
    ]

    return {"results": results}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8082)
