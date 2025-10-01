from lib.util import decode_bytes_to_str, encode_str_to_bytes
from lib.logger import get_logger
from confluent_kafka import Producer
from typing import Dict

class KafkaProducer:
    """
    A Kafka producer class that encapsulates the producer instance and provides
    methods for sending messages to Kafka topics.
    """
    
    def __init__(self, bootstrap_servers: str = 'localhost:9092'):
        """
        Initialize the Kafka producer.
        
        Args:
            bootstrap_servers (str): Kafka broker address(es)
        """
        self.logger = get_logger()

        self.config = {
            'bootstrap.servers': bootstrap_servers,
        }

        self.logger.info(f"Kafka producer configuration: {self.config}")
        self.logger.info("Initializing Kafka producer...")
        self.producer = Producer(self.config)
        self.logger.info("Kafka producer initialized successfully")
    
    def delivery_report(self, err, msg) -> None:
        """
        Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush().
        
        Args:
            err: Error object if delivery failed, None if successful
            msg: Message object containing delivery information
        """
        if err is not None:
            self.logger.error(f'Message delivery failed: {err}')
        else:
            decoded_message = decode_bytes_to_str(msg.value())
            self.logger.info(f'Delivering message: {decoded_message}')
            self.logger.info(f'Message delivered to {msg.topic()} [{msg.partition()}] @ offset {msg.offset()} and timestamp {msg.timestamp()}')
    
    def send_message(self, topic: str, message_data: Dict[str, str]) -> None:
        """
        Send a message to a Kafka topic.
        
        Args:
            topic (str): The Kafka topic to send the message to
            message_data (dict): The message data to send (will be converted to JSON)
        """
        # convert the message dict to bytes using the utility function
        self.logger.info(f"Serializing message data: {message_data} to bytes")
        raw = encode_str_to_bytes(message_data)
        self.logger.info(f"Serialized message data to bytes: {raw}")
        
        # produce the message to the specified topic
        self.producer.produce(topic, value=raw, callback=self.delivery_report)
    
    def close(self) -> None:
        """
        Close the producer and clean up resources.
        """
        if self.producer:
            # wait for any outstanding messages to be delivered and delivery reports to be received
            # kafka batches messages for efficiency so this is important to ensure delivery of the message
            self.producer.flush()
            self.logger.info("Kafka producer closed successfully")