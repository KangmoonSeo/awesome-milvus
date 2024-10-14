# coordinator_service/data_coordinator.py
from fastapi import FastAPI

app = FastAPI()


@app.post("/data_coordinator/flush")
def flush_data():
    # Trigger data flushing on data nodes
    return {"message": "Data flush triggered"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8083)
