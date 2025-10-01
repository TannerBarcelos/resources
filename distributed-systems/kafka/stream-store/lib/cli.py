import argparse

def parse_arguments():
    """
    Parse command-line arguments for the Kafka Stream Store application.
    
    Returns:
        argparse.Namespace: Parsed command-line arguments
    """
    parser = argparse.ArgumentParser(
        description='Kafka Stream Store - Generate and send fake orders to Kafka',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--num-orders', 
        type=int, 
        default=5,
        help='Number of fake orders to generate and send to Kafka (default: 5 for safe fallback)'
    )
    
    return parser.parse_args()