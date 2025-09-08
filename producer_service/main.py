import os
from config import PODCASTS_DIR
from file_reader import extract_metadata
from json_builder import build_json
from kafka_producer import send_to_kafka
from common.logger import Logger

PODCASTS_DIR = os.getenv("PODCASTS_DIR", "/host_podcasts")

logger = Logger.get_logger()

def main():
    """
    the entry point for producer Service
    """
    logger.info("Producer service started, scanning files..")

    # now iterate over all .wav files in the PODCASTS_DIR
    try:
        for file_name in os.listdir(PODCASTS_DIR):
            if file_name.endswith(".wav"):
                file_path = os.path.join(PODCASTS_DIR, file_name)
                metadata = extract_metadata(file_path)
                json_message = build_json(metadata)
                send_to_kafka(json_message)
                logger.info(f"file {file_name} processed and sent to Kafka successfully")
    except Exception as e:
        logger.error(f"Producer encountered an error: {e}")
        raise

if __name__ == "__main__":
    main()