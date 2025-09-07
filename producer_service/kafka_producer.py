from kafka import KafkaProducer
from config import KAFKA_BROKER, KAFKA_TOPIC
import logging

logging.basicConfig(level=logging.INFO)

def send_to_kafka(json_message: str):
    """
    now i send json message to Kafka topic
    """
    producer = KafkaProducer(
        # here is the list of kafka brokers
        bootstrap_servers=[KAFKA_BROKER],
        # serialize json message to utf-8
        value_serializer=lambda v: v.encode("utf-8")
    )
    producer.send(KAFKA_TOPIC, json_message)
    producer.flush()
    logging.info(f"Sent message to Kafka topic {KAFKA_TOPIC}")