from kafka import KafkaConsumer
import json
from config import KAFKA_BROKER, KAFKA_TOPIC
from common.logger import Logger

logger = Logger.get_logger()

def consume_messages():
    """
    finally consume messages from kafka topic and yield json objects
    so that other modules can process them
    """
    # here is the kafka consumer that reads from the topic
    try:
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
        logger.info(f"Connected to Kafka broker={KAFKA_BROKER}, topic={KAFKA_TOPIC}")

        # now continuously listen for messages (and yield them as they come)
        for message in consumer:
            logger.info(f"Consumed message from Kafka topic={KAFKA_TOPIC}, partition={message.partition}, offset={message.offset}")
            yield message.value

    except Exception as e:
        logger.error(f"Kafka consumer failed to connect or read messages: {e}")
        raise