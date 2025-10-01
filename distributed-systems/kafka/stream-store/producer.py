from lib.util import decode_bytes_to_str, encode_str_to_bytes
from lib.logger import get_logger
from lib.config import get_config
from confluent_kafka import Producer
from typing import Dict
from lib.orders import build_fake_orders
from lib.cli import parse_arguments
from lib.logger import get_logger

class KafkaProducer:
    """
    A Kafka producer class that encapsulates the producer instance and provides
    methods for sending messages to Kafka topics.
    """
    
    def __init__(self, bootstrap_servers: str = None):
        """
        Initialize the Kafka producer.
        
        Args:
            bootstrap_servers (str): Kafka broker address(es). If None, uses config value.
        """
        self.logger = get_logger()
        self.config = get_config()
        
        # Use provided bootstrap_servers or fall back to config
        bootstrap_servers = bootstrap_servers or self.config.get('kafka.bootstrap_servers', 'localhost:9092')

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
            self.logger.info("Kafka producer closed successfully")\

def run():
    # Initialize logger 
    logger = get_logger()
    config = get_config()

    # Parse command-line arguments
    logger.info("Parsing command-line arguments...")
    args = parse_arguments()
    logger.info(f"Arguments received: {args}")
    
    # Create a Kafka producer instance
    producer = KafkaProducer()

    # Build a list of fake orders for testing
    orders = build_fake_orders(args.num_orders)

    # Get topic name from config
    orders_topic = config.get('kafka.topics.orders', 'orders')
    
    logger.info(f"Generating and sending {args.num_orders} fake orders to Kafka...")

    for order in orders:
        # Send the order message to the orders topic
        producer.send_message(orders_topic, order)

    logger.info(f"Successfully sent {args.num_orders} orders to the '{orders_topic}' topic.")
    
    # Close the producer to ensure all messages are sent before exiting
    producer.close()

def main():
    run()

if __name__ == "__main__":
    main()