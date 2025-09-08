import speech_recognition as sr # i
from common.logger import Logger

logger = Logger.get_logger()

def transcribe_audio(file_path: str):
    """
    here i transcribe the audio file at file_path using SpeechRecognition library
    """
    ...