import pymongo
import pathlib
import gridfs
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

def save_file_to_mongo(unique_id: str, file_path: str):
    """
    here save the actual .wav file into mongoDB using GridFS
    """
    
    client = ...
    db = ...
    fs = ...
