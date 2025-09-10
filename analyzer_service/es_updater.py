from elasticsearch import Elasticsearch
from config import ES_HOST, ES_INDEX
from common.logger import Logger

logger = Logger.get_logger()

def update_analysis(unique_id: str, analysis: dict):
    """
    also update the Elasticsearch document with bds analysis results..
    """
    # connect to elasticsearch
    es = Elasticsearch(ES_HOST)
    try:
        es.update(
            index=ES_INDEX,
            id=unique_id,
            body={
                "doc": {
                    "bds_percent": analysis["bds_percent"],
                    "is_bds": analysis["is_bds"],
                    "bds_threat_level": analysis["bds_threat_level"]
                }
            },
            doc_as_upsert=True
        )
        logger.info(f"updated BDS analysis for ID={unique_id}")
    except Exception as e:
        logger.error(f"Failed to update BDs analysis for id={unique_id}: {e}")
        raise