import logging
from elasticsearch import Elasticsearch
from datetime import datetime, timezone
import os

class Logger:
    _logger = None

    @classmethod
    def get_logger(
        cls,
        name=os.getenv("LOGGER_NAME", "podcast_logger"),
        es_host=os.getenv("LOGGER_ES_HOST", "http://elasticsearch:9200"),
        index=os.getenv("LOGGER_ES_INDEX", "podcast_logs"),
        level=logging.INFO,
    ): 
        """
        return a singleton logger instance
        and logs go both to console and to elasticsearch.
        """
        if cls._logger:
            return cls._logger
        
        # create logger instance
        logger = logging.getLogger(name)
        logger.setLevel(level)

        # avoid duplicate handlers
        if not logger.handlers:
            # elasticsearch handler to log to elasticsearch
            es = Elasticsearch(es_host)

            class ESHandler(logging.Handler):
                # custom handler to send logs to elasticsearch 
                def emit(self, record):
                    try:
                        es.index(
                            index=index,
                            document={
                                "timestamp": datetime.now(timezone.utc).isoformat(),
                                "level": record.levelname,
                                "logger": record.name,
                                "message": record.getMessage(),
                            },
                        )
                    except Exception as e:
                        print(f"[Logger] failed to log to ES: {e}")

            # and add handlers to the logger
            logger.addHandler(ESHandler())
            logger.addHandler(logging.StreamHandler())

        cls._logger = logger
        return logger