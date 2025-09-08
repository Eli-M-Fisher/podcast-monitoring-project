from kafka import KafkaProducer
from config import KAFKA_BROKER, KAFKA_TOPIC
from common.logger import Logger

logger = Logger.get_logger()

def send_to_kafka(json_message: str):
    """
    now i send json message to Kafka topic
    """
    try:
        producer = KafkaProducer(
            # here is the list of kafka brokers
            bootstrap_servers=[KAFKA_BROKER],
            # serialize json message to utf-8
            value_serializer=lambda v: v.encode("utf-8")
        )
        # send the message to the topic
        producer.send(KAFKA_TOPIC, json_message)
        # and make sure all messages are sent (flush the buffer, means wait until all messages are sent (l.f))
        producer.flush()
        
        logger.info(f"Sent message to Kafka topic {KAFKA_TOPIC}")
    
    except Exception as e:
        logger.error(f"Failed to send message to kafka topic {KAFKA_TOPIC}: {e}")
        raise