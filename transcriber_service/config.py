import os

# a path to local podcasts directory
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "podcast-files")

# elasticsearch configuration
ES_HOST = os.getenv("ES_HOST", "http://elasticsearch:9200")
ES_INDEX = os.getenv("ES_INDEX", "podcasts_metadata")