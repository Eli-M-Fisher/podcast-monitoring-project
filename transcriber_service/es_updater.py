from elasticsearch import Elasticsearch
from config import ES_HOST, ES_INDEX
from common.logger import Logger

logger = Logger.get_logger()

def update_transcription(unique_id: str, transcription: str):
    """
    and update the transcription field for the document with unique id in elasticsearch
    """
    es = Elasticsearch(ES_HOST)
    try:
        es.update(
            index=ES_INDEX,
            id=unique_id,
            doc={"doc": {"transcription": transcription}}
        )
        logger.info(f"Updated transcription for ID={unique_id}")
    except Exception as e:
        logger.error(f"Failed to update transcription for ID={unique_id}: {e}")
        raise