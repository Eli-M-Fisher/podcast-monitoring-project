from kafka_consumer import consume_messages
from id_generator import generate_unique_id
from elastic_writer import write_metadata_to_es
from mongo_writer import save_file_to_mongo

def main():
    """
    entry point for producer Service
    """
    print("[Consumer] Starting consumer service..")
    for json_data in consume_messages():
        print(f"[Consumer] Received message: {json_data}")

        # start generate unique id
        unique_id = generate_unique_id(json_data)
        print(f"[Consumer] Generated unique_id: {unique_id}")

        # and write metadata to elasticsearch
        write_metadata_to_es(unique_id, json_data)

        # lastly save actual file into mongodb
        save_file_to_mongo(unique_id, json_data["path"])
    
if __name__ == "__main__":
    main()