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
        KAFKA_TOPIC,
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
        unique_id = data.get("id") or None

        if not file_path:
            logger.error("NO file path found in message")
            continue

        # and transcribe the audio file and update es
        try:
            transcription = transcribe_audio(file_path)
            if unique_id:
                update_transcription(unique_id, transcription)
            else:
                logger.error("No unique_id provided in message")
        except Exception as e:
            logger.error(f"Processing failed for message {data}: {e}")


if __name__ == "__main__":
    main()