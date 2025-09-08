import speech_recognition as sr # i
from common.logger import Logger

logger = Logger.get_logger()

def transcribe_audio(file_path: str) -> str:
    """
    here i transcribe the audio file at file_path using SpeechRecognition library
    """
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
        transcription = recognizer.recognize_google(audio)
        logger.info(f"Transcription completed for {file_path}")
        return transcription
    except Exception as e:
        logger.error(f"Failed to transcribe {file_path}: {e}")
        raise