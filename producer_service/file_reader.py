import pathlib
from constants import ERROR_FILE_NOT_FOUND
from common.logger import Logger

logger = Logger.get_logger()

def extract_metadata(file_path: str) -> dict:
    """
    here i extract metadata from a file path
    """
    # i check if the file exists
    path = pathlib.Path(file_path)
    logger.info(f"Tried to extract metadata for file: {file_path}")

    if not path.exists():
        logger.error(f"{ERROR_FILE_NOT_FOUND}: {file_path}")
        raise FileNotFoundError(f"{ERROR_FILE_NOT_FOUND}: {file_path}")
    
    # extract some basic metadata from the file path
    metadata = {
        "file_name": path.name,
        "file_size": path.stat().st_size,
        "created_at": path.stat().st_ctime,
        "path": str(path.resolve())
    }
    
    logger.info(f"Extracted metadata for file={path.name}, size={metadata['file_size']} bytes")
    return metadata