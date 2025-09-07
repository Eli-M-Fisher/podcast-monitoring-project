from elasticsearch import Elasticsearch
from config import ES_HOST, ES_INDEX

def write_metadata_to_es(unique_id: str, metadata: dict):
    """
    and write the metadata to elasticsearch  with unique id
    """
    ...