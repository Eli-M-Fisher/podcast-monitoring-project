from elasticsearch import Elasticsearch
from config import ES_HOST, ES_INDEX
from common.logger import Logger

logger = Logger.get_logger()

def update_transcription(unique_id: str, transcription: str):
    """
    Update transcription field for the document with the given unique_id in Elasticsearch
    """
    es = Elasticsearch(ES_HOST)
    try:
        es.update(
            index=ES_INDEX,
            id=unique_id,
            body={
                "doc": {"transcription": transcription}
            },
            doc_as_upsert=True
        )
        logger.info(f"Updated transcription for ID={unique_id}")

    except Exception as e:
        logger.error(f"Error while updating transcription for ID={unique_id}: {e}")
        raise