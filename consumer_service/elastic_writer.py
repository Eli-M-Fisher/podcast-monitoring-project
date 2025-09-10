from elasticsearch import Elasticsearch
from config import ES_HOST, ES_INDEX
from datetime import datetime, timezone
from common.logger import Logger

logger = Logger.get_logger()

def write_metadata_to_es(unique_id: str, metadata: dict):
    """
    and write the metadata to elasticsearch with unique id
    """
    try:
        es = Elasticsearch(ES_HOST)

        doc = {
            # i use the unique id as the document id in elasticsearch with the field name "id"
            "id": unique_id,
            # unpack the metadata dictionary into the document to be indexed
            **metadata,
            # add to myself an ingestion timestamp for record keeping 
            "ingested_at": datetime.now(timezone.utc).isoformat()
        }

        # upsert the document (insert or update if exists) use update with doc_as_upsert to avoid overwriting existing fields
        es.update(
            index=ES_INDEX,
            id=unique_id,
            body={"doc": doc},
            doc_as_upsert=True
        )

        logger.info(f"Upserted metadata in Elasticsearch (ID={unique_id})")

    except Exception as e:
        logger.error(f"Failed to index metadata in Elasticsearch (ID={unique_id}): {e}")
        raise
