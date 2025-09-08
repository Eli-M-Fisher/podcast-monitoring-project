from kafka import KafkaConsumer
import json
from config import KAFKA_BROKER, KAFKA_TOPIC

def consume_messages():
    """
    finally consume messages from kafka topic and yield json objects
    so that other modules can process them
    """
    # here is the kafka consumer that reads from the topic
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        # here is the list of kafka brokers (just one in my case now) (bootstrap means starting point (l.f))
        bootstrap_servers=[KAFKA_BROKER],
        # deserialize json message from utf-8 (string) to dict
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        # and start reading at the earliest message (if no offset is committed yet)
        auto_offset_reset="earliest",
        # and use this consumer group id (so that multiple consumers can share the load)
        group_id="podcast-consumer-group"
    )
    for message in consumer:
        yield message.value