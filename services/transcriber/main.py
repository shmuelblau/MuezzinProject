import time
from classes.manager import Manager
from config import *
from classes.logger import log


log.info(log.handlers)

time.sleep(20)


log.info(f"CONNECTION_STRING : {CONNECTION_STRING}")
log.info(f"DATABASE : {DATABASE}")
log.info(f"ELASTICSEARCH_HOST : {ELASTICSEARCH_HOST}")
log.info(f"ELASTICSEARCH_INDEX : {ELASTICSEARCH_INDEX}")




log.info("start")

manager = Manager(
    conn_mongo = CONNECTION_STRING ,
    db_name = DATABASE ,
    elastic_host= ELASTICSEARCH_HOST ,
    elastic_index= ELASTICSEARCH_INDEX,
    kafka_host= KAFKA_HOST,
    kafka_topic=KAFKA_TOPIC,
    new_topic= NEW_TOPIC
    )


manager.start_operations()

