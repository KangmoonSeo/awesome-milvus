# storage/log_broker.py
import pulsar
from config import PULSAR_SERVICE_URL


class LogBroker:
    def __init__(self):
        self.client = pulsar.Client(PULSAR_SERVICE_URL)

    def publish_message(self, topic, message):
        producer = self.client.create_producer(topic)
        producer.send(message.encode("utf-8"))
        producer.close()

    def subscribe_to_topic(self, topic, subscription_name):
        consumer = self.client.subscribe(topic, subscription_name)
        return consumer

    def close(self):
        self.client.close()
