import json

def build_json(metadata: dict):
    """
    and convert metadata dictionary into json string
    """
    # here i simply convert the metadata dictionary to a json string
    return json.dumps(metadata)