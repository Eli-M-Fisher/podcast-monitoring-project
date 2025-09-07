import os
from config import PODCASTS_DIR
from file_reader import extract_metadata
from json_builder import build_json
from kafka_producer import send_to_kafka

def main():
    """
    the entry point for producer Service
    """
    for file_name in os.listdir(PODCASTS_DIR):
        if file_name.endswith(".wav"):
            file_path = os.path.join(PODCASTS_DIR, file_name)
            metadata = extract_metadata(file_path)
            json_message = build_json(metadata)
            send_to_kafka(json_message)

if __name__ == "__main__":
    main()