import argparse
from lib.config import get_config

def parse_arguments():
    """
    Parse command-line arguments for the Kafka Stream Store application.
    
    Returns:
        argparse.Namespace: Parsed command-line arguments
    """
    config = get_config()
    default_num_orders = config.get('application.default_num_orders', 5)
    
    parser = argparse.ArgumentParser(
        description='Kafka Stream Store - Generate and send fake orders to Kafka',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--num-orders', 
        type=int, 
        default=default_num_orders,
        help=f'Number of fake orders to generate and send to Kafka (default: {default_num_orders} for safe fallback)'
    )
    
    return parser.parse_args()