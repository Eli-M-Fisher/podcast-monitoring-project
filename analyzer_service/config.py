import os

# kafka config
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "transcribed-files")

# elastic config
ES_HOST = os.getenv("ES_HOST", "http://elasticsearch:9200")
ES_INDEX = os.getenv("ES_INDEX", "podcasts_metadata_v2")

# encoded wordlists
HOSTILE_WORDS_ENCODED = os.getenv("HOSTILE_WORDS_ENCODED")
LESS_HOSTILE_WORDS_ENCODED = os.getenv("LESS_HOSTILE_WORDS_ENCODED")

# Optional: hostile pairs (comma-separated word1|word2)
HOSTILE_PAIRS = os.getenv("HOSTILE_PAIRS", "")