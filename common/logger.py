import logging
from elasticsearch import Elasticsearch
from datetime import datetime
import os

class Logger:
    _logger = None
    @classmethod
    def get_logger():
        
        """
        return a singleton logger instance
        and logs go both to console and to elasticsearch.
        """

        # avoid duplicate handlers

        # and add handlers