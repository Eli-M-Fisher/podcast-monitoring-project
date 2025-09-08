from kafka_consumer import consume_messages
from id_generator import generate_unique_id
from elastic_writer import write_metadata_to_es
from mongo_writer import save_file_to_mongo
from common.logger import Logger

logger = Logger.get_logger()

def main():
    """
    entry point for producer Service
    """
    logger.info("Consumer service started, waiting for messages..")

    try:
        for json_data in consume_messages():
            logger.info(f"Received message from Kafka: {json_data}")
            # start generate unique id
            unique_id = generate_unique_id(json_data)
            logger.info(f"Generated unique_id: {unique_id}")

            # and write metadata to elasticsearch
            write_metadata_to_es(unique_id, json_data)
            logger.info(f"Metadata indexed in Elasticsearch (ID={unique_id})")

            # lastly save actual file into mongodb
            save_file_to_mongo(unique_id, json_data["path"])
            logger.info(f"File saved in mongodb (ID={unique_id})")
        
    except Exception as e:
        logger.error(f"Consumer encountered an error: {e}")
        raise
    
if __name__ == "__main__":
    main()