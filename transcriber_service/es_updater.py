from elasticsearch import Elasticsearch
from config import ES_HOST, ES_INDEX
from common.logger import Logger

logger = Logger.get_logger()

def update_transcription(unique_id: str, transcription: str):
    """
    and update the transcription field for the document with unique id in elasticsearch
    """
    ...
    