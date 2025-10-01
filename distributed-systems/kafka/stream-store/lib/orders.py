from typing import Dict, List
from faker import Faker

fake = Faker()

type Order = Dict[str, str]
type Orders = List[Order]

def build_fake_orders(num_orders: int = 5) -> Orders:
    """
    Build a list of fake order messages for testing purposes.
    Args:
        num_orders (int): Number of fake orders to generate (default is 5)
    Returns:
        List of fake order dictionaries
    """
    orders: Orders = []
    for _ in range(num_orders):
        order: Order = {
            'order_id': fake.uuid4(),
            'item_id': fake.uuid4(),
            'item': fake.word(),
            'quantity': fake.random_int(min=1, max=10),
            'user': fake.user_name()
        }
        orders.append(order)
    return orders
