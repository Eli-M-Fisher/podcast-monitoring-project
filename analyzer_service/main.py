from kafka import KafkaConsumer
import json
from config import KAFKA_BROKER, KAFKA_TOPIC
from analyzer import analyze_transcription
from es_updater import update_analysis
from common.logger import Logger

logger = Logger.get_logger()

def main():
    # now first create a kafka consumer to listen to the topic
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=[KAFKA_BROKER],
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset="earliest",
        group_id="analyzer-group" # should be different from transcriber group (l.f)
    )
    logger.info(f"Analyzer service started, listening to topic={KAFKA_TOPIC}")

    # continuously process messages from kafka
    for message in consumer:
        data = message.value
        transcription = data.get("transcription")
        unique_id = data.get("id")

        if not transcription or not unique_id:
            logger.error(f"Invalid message, missing transcription or id: {data}")
            continue

        # now i analyze the transcription and update the analysis field in es
        try:
            analysis = analyze_transcription(transcription)
            update_analysis(unique_id, analysis)
            logger.info(f"Analysis completed and updated for ID={unique_id}")
        except Exception as e:
            logger.error(f"Failed to process message {data}: {e}")
    
if __name__ == "__main__":
    main()