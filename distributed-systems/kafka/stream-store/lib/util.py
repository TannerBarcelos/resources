import json
from lib.config import get_config

encoding = 'utf-8'

def encode_str_to_bytes(s: str | dict) -> bytes:
    """Helper function to encode a string or dictionary to bytes using UTF-8 encoding. If a dictionary is provided, it will be converted to a JSON string before encoding to properly stringify it.
    Arguments:
        s (str | dict): The string or dictionary to encode
    Returns:
        bytes: The encoded bytes
    """
    if isinstance(s, dict):
        s = json.dumps(s)
    return s.encode(encoding)

def decode_bytes_to_str(b: bytes) -> str | dict:
    """Helper function to decode bytes to a string or dictionary using UTF-8 encoding."""
    decoded = b.decode(encoding)
    try:
        return json.loads(decoded)
    except json.JSONDecodeError:
        return decoded

def prettify_json(data: dict | str, indent: int = None) -> str:
    """Helper function to prettify JSON data with configurable indentation."""
    if indent is None:
        config = get_config()
        indent = config.get('formatting.json_indent', 2)
    
    return json.dumps(data, indent=indent)