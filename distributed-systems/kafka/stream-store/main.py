from kafka.producer import KafkaProducer
from lib.orders import build_fake_orders
from lib.cli import parse_arguments
from lib.logger import get_logger

def run():
    # Initialize logger 
    logger = get_logger()

    # Parse command-line arguments
    logger.info("Parsing command-line arguments...")
    args = parse_arguments()
    logger.info(f"Arguments received: {args}")
    
    # Create a Kafka producer instance
    producer = KafkaProducer()

    # Build a list of fake orders for testing
    orders = build_fake_orders(args.num_orders)

    logger.info(f"Generating and sending {args.num_orders} fake orders to Kafka...")

    for order in orders:
        # Send the order message to the 'orders' topic
        producer.send_message('orders', order)

    logger.info(f"Successfully sent {args.num_orders} orders to the 'orders' topic.")
    
    # Close the producer to ensure all messages are sent before exiting
    producer.close()

def main():
    run()

if __name__ == "__main__":
    main()
