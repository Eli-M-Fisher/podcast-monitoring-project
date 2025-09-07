from elasticsearch import Elasticsearch
from config import ES_HOST, ES_INDEX

def write_metadata_to_es(unique_id: str, metadata: dict):
    """
    and write the metadata to elasticsearch  with unique id
    """
    es = Elasticsearch(ES_HOST)

    doc = {
        "id": unique_id,
        **metadata,
        "ingested_at": datetime.utcnow().isoformat()
    }

    es.index(index=ES_INDEX, id=unique_id, document=doc)
    print(f"[Elasticsearch] Indexed document with ID: {unique_id}")