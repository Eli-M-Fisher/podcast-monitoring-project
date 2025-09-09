from kafka_consumer import consume_messages
from id_generator import generate_unique_id
from elastic_writer import write_metadata_to_es
from mongo_writer import save_file_to_mongo
from common.logger import Logger
from kafka import KafkaProducer
import json
from config import KAFKA_BROKER

logger = Logger.get_logger()

# first i initialize Kafka producer for processed-files topic
producer = KafkaProducer(
    # here is the list of kafka brokers
    bootstrap_servers=[KAFKA_BROKER],
    # serialize json message to utf-8
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def publish_processed_message(data: dict):
    """
    now publish processed file metadata (including unique id!) to a new Kafka topic 'processed-files so that transcriber service can consume it and transcribe the audio file
    and update the transcription in elasticsearch
    """
    # publish to processed-files topic (means the file has been processed and metadata is indexed in es and file is saved in mongo(l.f))
    try:
        producer.send("processed-files", data)
        producer.flush()
        logger.info(f"Published processed message to 'processed-files': {data}")
    except Exception as e:
        logger.error(f"Failed to publish processed message: {e}")
        raise

def main():
    """
    entry point for producer Service
    """
    logger.info("Consumer service started, waiting for messages..")

    try:
        for json_data in consume_messages():
            logger.info(f"Received message from Kafka: {json_data}")
            # start generate unique id based on file content
            unique_id = generate_unique_id(json_data["path"])
            logger.info(f"Generated unique_id: {unique_id}")

            # and write metadata to elasticsearch
            write_metadata_to_es(unique_id, json_data)
            logger.info(f"Metadata indexed in Elasticsearch (ID={unique_id})")

            # lastly save actual file into mongodb
            save_file_to_mongo(unique_id, json_data["path"])
            logger.info(f"File saved in mongodb (ID={unique_id})")

            # and now publish enriched message to processed-files topic
            processed_message = {
                "id": unique_id,
                "file_name": json_data.get("file_name"),
                "file_size": json_data.get("file_size"),
                "created_at": json_data.get("created_at"),
                "path": json_data.get("path")
            }
            logger.info(f"Processed message prepared: {processed_message}")

            publish_processed_message(processed_message)

        
    except Exception as e:
        logger.error(f"Consumer encountered an error: {e}")
        raise
    
if __name__ == "__main__":
    main()