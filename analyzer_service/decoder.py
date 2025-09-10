import base64
from common.logger import Logger

logger = Logger.get_logger()

def decode_wordlist(encoded_str: str) -> list[str]:
    """
    here i decode a base64 encoded comma-separated wordlist into a Python list...
    the words /phrases are separated by commas
    """
    try:
        decoded_bytes = base64.b64decode(encoded_str)
        decoded_str = decoded_bytes.decode("utf-8")
        items = [item.strip() for item in decoded_str.split(",") if item.strip()]
        logger.info(f"Decoded wordlist with {len(items)} items")
        return items
    except Exception as e:
        logger.error(f"Failed to decode wordlist: {e}")
        raise