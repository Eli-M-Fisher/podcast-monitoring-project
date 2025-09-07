import pymongo
import pathlib
import gridfs
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

def save_file_to_mongo(unique_id: str, file_path: str):
    """
    here save the actual .wav file into mongoDB using GridFS
    """
    client = pymongo.MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    fs = gridfs.GridFS(db, collection=MONGO_COLLECTION)

    path = pathlib.Path(file_path)
    with open(path, "rb") as f:
        file_id = fs.put(f, filename=path.name, unique_id=unique_id)
        print(f"[MongoDB] Stored file {path.name} with unique_id={unique_id}, file_id={file_id}")