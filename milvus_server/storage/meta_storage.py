# storage/meta_storage.py
import etcd3
from config import ETCD_HOST, ETCD_PORT


class MetaStorage:
    def __init__(self):
        self.client = etcd3.client(host=ETCD_HOST, port=ETCD_PORT)

    def save_metadata(self, key, value):
        self.client.put(key, value)

    def get_metadata(self, key):
        value, _ = self.client.get(key)
        return value.decode() if value else None
