import hashlib
import pathlib
from common.logger import Logger

logger = Logger.get_logger()

def generate_unique_id(file_path: str) -> str:
    """
    here i generate a stable unique id for a file based on its full content.
    This ensures that the same file always gets the same ID, 
    and different files always get different IDs.
    """
    path = pathlib.Path(file_path)

    if not path.exists():
        logger.error(f"File not found for unique_id generation: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # read file in chunks to avoid loading big files fully into memory
        sha256 = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256.update(chunk)

        unique_id = sha256.hexdigest()
        logger.info(f"Generated unique_id={unique_id} for file={path.name}")
        return unique_id

    except Exception as e:
        logger.error(f"Failed to generate unique_id for {file_path}: {e}")
        raise