import time
time.sleep(30)
from classes.manager import Manager
from config import *
from classes.logger import log

log.info("new v")
log.info(log.handlers)




log.info(f"HOST : {KAFKA_HOST}")
log.info(f"TOPIC_NAME : {TOPIC_NAME}")
log.info(f"CONNECTION_STRING : {CONNECTION_STRING}")
log.info(f"DATABASE : {DATABASE}")
log.info(f"ELASTICSEARCH_HOST : {ELASTICSEARCH_HOST}")
log.info(f"ELASTICSEARCH_INDEX : {ELASTICSEARCH_INDEX}")




log.info("start")

manager = Manager(
    kafka_host=KAFKA_HOST ,
    topic_name=TOPIC_NAME ,
    conn_mongo=CONNECTION_STRING ,
    db_name=DATABASE ,
    elastic_host=ELASTICSEARCH_HOST ,
    elastic_index=ELASTICSEARCH_INDEX
    )


manager.start_operations()

