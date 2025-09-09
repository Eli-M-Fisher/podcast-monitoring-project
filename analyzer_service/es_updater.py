from elasticsearch import Elasticsearch
from config import ES_HOST, ES_INDEX
from common.logger import Logger

logger = Logger.get_logger()

def update_analysis(unique_id: str, analysis: dict):
    ...