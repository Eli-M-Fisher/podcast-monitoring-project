import whisper
from common.logger import Logger
import pathlib

logger = Logger.get_logger()

# load model once (small/medium for speed, large for accuracy)
model = whisper.load_model("small")

def transcribe_audio(file_path: str) -> str:
    """
    here i transcribe audio file using Whisper model and return the transcription text
    i use the small model for speed, but medium or large would be more accurate
    """
    try:
        path = pathlib.Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        logger.info(f"Whisper: starting transcription for {file_path}")
        result = model.transcribe(str(path))
        transcription = result.get("text", "").strip()

        if not transcription:
            logger.warning(f"Whisper: no transcription produced for {file_path}")
        else:
            logger.info(f"Whisper transcription done for {file_path}")

        return transcription

    except Exception as e:
        logger.error(f"Whisper failed to transcribe {file_path}: {e}")
        raise