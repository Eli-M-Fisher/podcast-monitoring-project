from kafka import KafkaConsumer
import json
from config import KAFKA_BROKER, KAFKA_TOPIC
from transcriber import transcribe_audio
from es_updater import update_transcription
from common.logger import Logger

logger = Logger.get_logger()

def main():
    ...