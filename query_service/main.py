from fastapi import FastAPI, Query
from query_engine import get_by_id, get_by_threat, search_by_keyword, get_stats

app = FastAPI(title="Podcast Query Service", version="1.0.0")

@app.get("/query/by_id/{unique_id}")
def query_by_id(unique_id: str):
    return get_by_id(unique_id)

@app.get("/query/by_threat/{level}")
def query_by_threat(level: str):
    return get_by_threat(level)

@app.get("/query/search")
def query_search(keyword: str = Query(..., description="keyword to saerch in transcription")):
    return search_by_keyword(keyword)

@app.get("/query/stats")
def query_stats():
    return get_stats()