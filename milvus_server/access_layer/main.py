# access_layer/main.py
from fastapi import FastAPI, HTTPException
from models.models import Collection, QueryRequest
import requests

app = FastAPI()

collections = {}


@app.post("/collections")
def create_collection(collection: Collection):
    if collection.name in collections:
        raise HTTPException(status_code=400, detail="Collection already exists")
    response = requests.post(
        "http://localhost:8081/root_coordinator/create_collection",
        json=collection.dict(),
    )
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to create collection")
    collections[collection.name] = collection
    return {"message": "Collection created"}


@app.delete("/collections/{collection_name}")
def delete_collection(collection_name: str):
    if collection_name not in collections:
        raise HTTPException(status_code=404, detail="Collection not found")
    response = requests.delete(
        f"http://localhost:8081/root_coordinator/delete_collection/{collection_name}"
    )
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to delete collection")
    del collections[collection_name]
    return {"message": "Collection deleted"}


@app.post("/query")
def search(query_request: QueryRequest):
    if query_request.collection not in collections:
        raise HTTPException(status_code=404, detail="Collection not found")
    response = requests.post(
        "http://localhost:8082/query_node/search", json=query_request.dict()
    )
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Query execution failed")
    return response.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
