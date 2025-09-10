from kafka import KafkaConsumer, KafkaProducer
import json
from config import KAFKA_BROKER, KAFKA_TOPIC
from transcriber import transcribe_audio
from es_updater import update_transcription
from common.logger import Logger

logger = Logger.get_logger()

# first initialize kafka producer for sending transcribed results
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def publish_transcribed_message(unique_id: str, transcription: str):
    """
    Publish a transcribed message to the 'transcribed-files' topic
    so that the analyzer service can consume and analyze it.
    """
    try:
        message = {"id": unique_id, "transcription": transcription}
        producer.send("transcribed-files", message)
        producer.flush()
        logger.info(f"Published transcribed message to 'transcribed-files': {message}")
    except Exception as e:
        logger.error(f"Failed to publish transcribed message for ID={unique_id}: {e}")
        raise


def main():
    # create a Kafka consumer to listen to the topic
    consumer = KafkaConsumer(
        KAFKA_TOPIC,  # should default to "processed-files" and not "podcasts" (l.f)
        bootstrap_servers=[KAFKA_BROKER],
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset="earliest",
        group_id="transcriber-group"
    )
    logger.info(f"Transcriber service started, listening to topic={KAFKA_TOPIC}")

    # continuously process messages from Kafka
    for message in consumer:
        data = message.value
        file_path = data.get("path")
        unique_id = data.get("id") # should have unique id to update the right document in es (l.f)

        if not file_path or not unique_id:
            logger.error(f"Invalid message received, missing file_path or unique_id: {data}")
            continue

        try:
            # runing transcription
            transcription = transcribe_audio(file_path)
            # and update transcription in Elasticsearch
            update_transcription(unique_id, transcription)
            # and publish to Kafka for analyzer
            publish_transcribed_message(unique_id, transcription)

            logger.info(f"Transcription completed, updated in ES, and published to Kafka (ID={unique_id})")

        except Exception as e:
            logger.error(f"Processing failed for message {data}: {e}")

if __name__ == "__main__":
    main()