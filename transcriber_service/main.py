from kafka import KafkaConsumer
import json
from config import KAFKA_BROKER, KAFKA_TOPIC
from transcriber import transcribe_audio
from es_updater import update_transcription
from common.logger import Logger

logger = Logger.get_logger()

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
            transcription = transcribe_audio(file_path)
            update_transcription(unique_id, transcription) # update transcription in es
            logger.info(f"Transcription completed and updated in es (ID={unique_id})")
        except Exception as e:
            logger.error(f"processing failed for message {data}: {e}")

if __name__ == "__main__":
    main()