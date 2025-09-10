from fastapi import FastAPI, Query
from query_engine import get_by_id, get_by_threat, search_by_keyword, get_stats

app = FastAPI(title="Podcast Query Service", version="1.0.0")

# endpoint to get document by unique_id
@app.get("/query/by_id/{unique_id}")
def query_by_id(unique_id: str):
    return get_by_id(unique_id)

# endpoint to get documents by threat level
@app.get("/query/by_threat/{level}")
def query_by_threat(level: str):
    return get_by_threat(level)

# endpoint to search documents by keyword in transcription
@app.get("/query/search")
def query_search(keyword: str = Query(..., description="keyword to saerch in transcription")):
    return search_by_keyword(keyword)

# and endpoint to get stats
@app.get("/query/stats")
def query_stats():
    return get_stats()