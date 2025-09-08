import hashlib
import json

def generate_unique_id(data: dict) -> str:
    """
    first generate a unique id from the json data using sha256 hash
    """
    # ensure consistent ordering by sorting the keys by converting to a string
    json_str = json.dumps(data, sort_keys=True)
    # then hash the string to generate a unique id
    return hashlib.sha256(json_str.encode("utf-8")).hexdigest()