# This consumer represents a tracker, or audit log, that processes and logs all orders.

import json
from confluent_kafka import Consumer

from lib.logger import get_logger
from lib.util import decode_bytes_to_str, prettify_json

class KafkaConsumer:
    """
    A Kafka consumer class that encapsulates the consumer instance and provides
    methods for consuming messages from Kafka topics.
    """
    def __init__(self, bootstrap_servers: str = 'localhost:9092', group_id: str = 'order-tracker'):
        self.logger = get_logger()
        self.config = {
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,  # consumer group id of the group this consumer service belongs to (if we scaled this to 10 pods in kubernetes, they would all share the same group id within a consumer group)
            'auto.offset.reset': 'earliest' # start reading at the earliest message if no committed offsets exist
        }
        self.logger.info(f"Kafka consumer configuration: {self.config}")
        self.logger.info("Initializing Kafka consumer...")
        self.consumer = Consumer(self.config)

        self.logger.info("Kafka consumer initialized successfully")
        topics = ['orders']
        self.consumer.subscribe(topics) #subscribe takes a list of topics to subscribe to, in this case just one topic 'orders'
        self.logger.info("Subscribed to 'orders' topic")

    def consume_messages(self):
        """
        Continuously poll for messages from the subscribed topics and process them.
        """
        try:
            while True:
                msg = self.consumer.poll(1.0)  # timeout of 1 second
                if msg is None:
                    continue
                if msg.error():
                    self.logger.error(f"Consumer error: {msg.error()}")
                    continue
                deserialized = decode_bytes_to_str(msg.value())
                self.logger.info(f"Received order: {prettify_json(deserialized)}") # pretty print the JSON message
        # Handle any cleanup or finalization here - users will do ctrl+c to exit, which should raise a KeyboardInterrupt and be expected for graceful shutdown
        except KeyboardInterrupt:
            pass
        finally:
            self.close()

    def close(self) -> None:
        """
        Close the consumer and clean up resources.
        """
        if self.consumer:
            self.logger.info("Closing Kafka consumer...")
            self.consumer.close()
            self.logger.info("Kafka consumer closed successfully")

if __name__ == "__main__":
    consumer = KafkaConsumer()
    consumer.consume_messages()