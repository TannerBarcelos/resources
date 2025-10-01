import json

def encode_str_to_bytes(s: str | dict) -> bytes:
    """Helper function to encode a string or dictionary to bytes using UTF-8 encoding."""
    if isinstance(s, dict):
        s = json.dumps(s)
    return s.encode('utf-8')

def decode_bytes_to_str(b: bytes) -> str | dict:
    """Helper function to decode bytes to a string or dictionary using UTF-8 encoding."""
    decoded = b.decode('utf-8')
    try:
        return json.loads(decoded)
    except json.JSONDecodeError:
        return decoded