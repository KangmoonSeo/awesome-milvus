# storage/object_storage.py
from minio import Minio
from config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET_NAME


class ObjectStorage:
    def __init__(self):
        self.client = Minio(
            MINIO_ENDPOINT,
            access_key=MINIO_ACCESS_KEY,
            secret_key=MINIO_SECRET_KEY,
            secure=False,
        )
        if not self.client.bucket_exists(MINIO_BUCKET_NAME):
            self.client.make_bucket(MINIO_BUCKET_NAME)

    def upload_object(self, object_name, file_path):
        self.client.fput_object(MINIO_BUCKET_NAME, object_name, file_path)

    def download_object(self, object_name, file_path):
        self.client.fget_object(MINIO_BUCKET_NAME, object_name, file_path)
