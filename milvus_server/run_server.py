# run_server.py
import subprocess
import time
from config import MINIO_ACCESS_KEY, MINIO_SECRET_KEY


def start_minio():
    """Start MinIO using Docker."""
    try:
        subprocess.run(
            [
                "docker",
                "run",
                "-d",
                "-p",
                "9000:9000",
                "-p",
                "9001:9001",
                "--name",
                "minio",
                "-e",
                f"MINIO_ACCESS_KEY={MINIO_ACCESS_KEY}",
                "-e",
                f"MINIO_SECRET_KEY={MINIO_SECRET_KEY}",
                "minio/minio",
                "server",
                "/data",
            ]
        )
        print("Starting MinIO...")
        time.sleep(5)  # Wait for MinIO to start
    except Exception as e:
        print(f"Failed to start MinIO: {e}")


services = [
    ("access_layer.main", 8000),
    ("coordinator_service.root_coordinator", 8081),
    ("worker_nodes.query_node", 8082),
    ("coordinator_service.data_coordinator", 8083),
]

processes = []

if __name__ == "__main__":
    start_minio()  # Start MinIO

    try:
        for service, port in services:
            proc = subprocess.Popen(["uvicorn", f"{service}:app", "--port", str(port)])
            processes.append(proc)

        for proc in processes:
            proc.wait()
    except KeyboardInterrupt:
        for proc in processes:
            proc.terminate()
