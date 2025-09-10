from elasticsearch import Elasticsearch
from config import ES_HOST, ES_INDEX
from common.logger import Logger

logger = Logger.get_logger()

es = Elasticsearch(ES_HOST)

def get_by_id(unique_id: str) -> dict:
    ...

def get_by_threat(level: str) -> list[dict]:
    ...

def search_by_keyword(keyword: str) -> list[dict]:
    ...

def get_stats() -> dict:
    ...