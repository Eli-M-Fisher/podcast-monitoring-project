import pymongo
import pathlib
import gridfs # i disided to use gridfs to handle large files in mongodb because podcast .wav files can be large 
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

def save_file_to_mongo(unique_id: str, file_path: str):
    """
    here save the actual .wav file into mongoDB using GridFS
    """
    # connect to mongoDb
    client = pymongo.MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    # use gridfs to handle large files
    fs = gridfs.GridFS(db, collection=MONGO_COLLECTION)

    # read the file and save to mongodB
    path = pathlib.Path(file_path)
    with open(path, "rb") as f: # ("rb") to read binary files like .wav (l.f)
        # store the file with unique_id as metadata
        file_id = fs.put(f, filename=path.name, unique_id=unique_id)
        print(f"[MongoDB] Stored file {path.name} with unique_id={unique_id}, file_id={file_id}")