from kafka import KafkaConsumer
import json
from config import KAFKA_BROKER, KAFKA_TOPIC

def consume_messages():
    """
    finally consume messages from kafka topic and yield json objects
    so that other modules can process them
    """
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=[KAFKA_BROKER],
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset="earliest",
        group_id="podcast-consumer-group"
    )
    for message in consumer:
        yield message.value