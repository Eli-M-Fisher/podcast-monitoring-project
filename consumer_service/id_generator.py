import hashlib
import json

def generate_unique_id(data: dict) -> str:
    """
    first generate a unique id from the json data using sha256 hash
    """
    json_str = json.dumps(data, sort_keys=True)
    return hashlib.sha256(json_str.encode("utf-8")).hexdigest()