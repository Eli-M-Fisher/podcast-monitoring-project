import os

# kafka config
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "transcribed-files")

# elastic config
ES_HOST = os.getenv("ES_HOST", "http://elasticsearch:9200")
ES_INDEX = os.getenv("ES_INDEX", "podcasts_metadata_v2")

# encoded wordlists
HOSTILE_WORDLIST_BASE64 = os.getenv("HOSTILE_WORDLIST_BASE64")
LESS_HOSTILE_WORDLIST_BASE64 = os.getenv("LESS_HOSTILE_WORDLIST_BASE64")

# the analyzer thresholds (in percents)
BDS_THRESHOLD = float(os.getenv("BDS_THRESHOLD", "5.0"))
MEDIUM_THRESHOLD = float(os.getenv("MEDIUM_THRESHOLD", "2.0"))
HIGH_THRESHOLD = float(os.getenv("HIGH_THRESHOLD", "10.0"))