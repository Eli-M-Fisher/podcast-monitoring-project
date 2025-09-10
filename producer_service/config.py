import os

# here is a path to local podcasts directory
PODCASTS_DIR = os.getenv("PODCASTS_DIR", "/Users/elifisher/Downloads/podcasts")

# and kafka configuration
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
KAFKA_TOPIC = os.getenv("PRODUCER_TOPIC", "podcast-files")