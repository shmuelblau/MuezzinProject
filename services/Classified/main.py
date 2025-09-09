import time
from classes.manager import Manager
from config import *
from classes.logger import log


log.info(log.handlers)

log.info(f"ELASTICSEARCH_HOST : {ELASTICSEARCH_HOST}")
log.info(f"ELASTICSEARCH_INDEX : {ELASTICSEARCH_INDEX}")




log.info("start")

manager = Manager(
    elastic_host= ELASTICSEARCH_HOST ,
    elastic_index= ELASTICSEARCH_INDEX,
    kafka_host=KAFKA_HOST,
    new_topic=NEW_TOPIC

    
    )



manager.start_operations()

