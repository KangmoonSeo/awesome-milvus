# coordinator_service/root_coordinator.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
collections: Dict[str, dict] = {}

class Collection(BaseModel):
    name: str
    description: str

@app.post("/root_coordinator/create_collection")
def create_collection(collection: Collection):
    if collection.name in collections:
        raise HTTPException(status_code=400, detail="Collection already exists")
    collections[collection.name] = {"description": collection.description}
    return {"message": "Collection created successfully"}

@app.delete("/root_coordinator/delete_collection/{collection_name}")
def delete_collection(collection_name: str):
    if collection_name not in collections:
        raise HTTPException(status_code=404, detail="Collection not found")
    del collections[collection_name]
    return {"message": "Collection deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
