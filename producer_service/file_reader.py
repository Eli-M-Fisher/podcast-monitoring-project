import pathlib
from constants import ERROR_FILE_NOT_FOUND

def extract_metadata(file_path: str):
    path = pathlib.Path(file_path)
    """
    here i extract metadata from a file path
    """
    return metadata