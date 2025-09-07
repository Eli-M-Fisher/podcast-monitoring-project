from kafka_consumer import consume_messages
from id_generator import generate_unique_id
from elastic_writer import write_metadata_to_es
from mongo_writer import save_file_to_mongo

def main():
    """
    entry point for producer Service
    """
    # start generate unique id

    # and write metadata to elasticsearch

    # lastly save actual file into mongodb
    
if __name__ == "__main__":
    main()