import json

def build_json(metadata: dict):
    """
    and convert metadata dictionary into json string
    """
    return json.dumps(metadata)