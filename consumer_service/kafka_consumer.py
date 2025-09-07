from kafka import KafkaConsumer
import json
from config import KAFKA_BROKER, KAFKA_TOPIC

def consume_messages():
    """
    finally consume messages from kafka topic and yield json objects
    so that other modules can process them
    """
    ...

