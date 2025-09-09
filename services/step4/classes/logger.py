import functools
from config import *
import logging
from elasticsearch import Elasticsearch
from datetime import datetime

# def get_logger():
#     logger = logging.getLogger("console_logger")
#     logger.setLevel(logging.INFO)
#     if not logger.handlers:
#         handler = logging.StreamHandler()
#         formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%d-%m-%Y %H:%M:%S")
#         handler.setFormatter(formatter)
#         logger.addHandler(handler)
#     return logger


class createLogger:
    _logger = None
    @classmethod
    def get_logger(cls, name=ELASTICSEARCH_LOGS_INDEX, es_host=ELASTICSEARCH_HOST,
        index=ELASTICSEARCH_LOGS_INDEX, level=logging.INFO):
        
        if cls._logger:
            
            return cls._logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            es = Elasticsearch(f'http://{es_host}:{9200}')
            
            class ESHandler(logging.Handler):
                def emit(self, record):
                    try:
                        es.index(index=index, document={
                        "timestamp": datetime.utcnow().isoformat(),

                        "level": record.levelname,
                        "logger": record.name,
                        "message": record.getMessage()

                        })
                    except Exception as e:
                        print(f"ES log failed: {e}")
            handler = logging.StreamHandler() 
            formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%d-%m-%Y %H:%M:%S")
            handler.setFormatter(formatter)

            logger.addHandler(ESHandler())
            logger.addHandler(handler)



        cls._logger = logger
        print("return a new logger")
        return logger

log = createLogger.get_logger()

def Logger(_func=None, *, log_start=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if log_start:
                log.info(f"start func: {func.__name__}")
            try:
                result = func(*args, **kwargs)
                if log_start:
                    log.info(f" finish func: {func.__name__}")
                return result
            except Exception as e:
                log.error(f"{func.__name__}: {e}", exc_info=True)
                raise
        return wrapper
    if _func is None:
        return decorator
    else:
        return decorator(_func)




