import json
from common.logger import Logger

logger = Logger.get_logger()

def build_json(metadata: dict) -> str:
    """
    and convert metadata dictionary into json string
    """
    # here i simply convert the metadata dictionary to a json string
    try:
        return json.dumps(metadata)
    except Exception as e:
        logger.error(f"Failed to build json from metadata; {e}")
        raise