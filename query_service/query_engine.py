from elasticsearch import Elasticsearch
from config import ES_HOST, ES_INDEX
from common.logger import Logger

logger = Logger.get_logger()

es = Elasticsearch(ES_HOST)

# simple get by id function
def get_by_id(unique_id: str) -> dict:
    try:
        doc = es.get(index=ES_INDEX, id=unique_id)
        return doc["_source"]
    except Exception as e:
        logger.error(f"Failed to fetch doc by id={unique_id}: {e}")
        raise

# get all documents with a specific threat level (like"low", "medium", "high" (l.f))
def get_by_threat(level: str) -> list[dict]:
    try:
        resp = es.search(
            index=ES_INDEX,
            query={"match": {"bds_threat_level": level}}
        )
        return [hit["_source"] for hit in resp["hits"]["hits"]]
    except Exception as e:
        logger.error(f"Failed to fetch docs by threat level={level}: {e}")
        raise


# here i cen search documents by keyword in transcription field
def search_by_keyword(keyword: str) -> list[dict]:
    try:
        resp = es.search(
            index=ES_INDEX,
            query={"match": {"transcription": keyword}}
        )
        return [hit["_source"] for hit in resp["hits"]["hits"]]
    except Exception as e:
        logger.error(f"Failed to search docs by keyword={keyword}: {e}")
        raise


# get some basic stats like counts of bds vs non-bds and threat levels (i use aggregations (means summary the data)l.f)
def get_stats() -> dict:
    try:
        # aggregation query to get counts of is_bds and threat levels
        resp = es.search(
            index=ES_INDEX,
            size=0,
            aggs={
                "is_bds_counts": {"terms": {"field": "is_bds"}},
                "threat_levels": {"terms": {"field": "bds_threat_level"}}
            }
        )
        # and return the aggregation results as a dictionary
        stats = {
            "is_bds": resp["aggregations"]["is_bds_counts"]["buckets"],
            "threat_levels": resp["aggregations"]["threat_levels"]["buckets"],
        }
        return stats
    
    except Exception as e:
        logger.error(f"Failed to fetch stats: {e}")
        raise