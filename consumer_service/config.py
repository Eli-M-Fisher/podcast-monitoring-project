import os

# the kafka configuration
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
KAFKA_TOPIC = os.getenv("CONSUMER_TOPIC", "podcast-files")

# elasticsearch configuration
ES_HOST = os.getenv("ES_HOST", "http://elasticsearch:9200")
ES_INDEX = os.getenv("ES_INDEX", "podcasts_metadata_v2")

# mongoDB configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
MONGO_DB = os.getenv("MONGO_DB", "podcasts_db")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "podcasts_files")