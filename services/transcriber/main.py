
from classes.manager import Manager
from config import *
from classes.logger import log


log.info(log.handlers)




log.info(f"CONNECTION_STRING : {CONNECTION_STRING}")
log.info(f"DATABASE : {DATABASE}")
log.info(f"ELASTICSEARCH_HOST : {ELASTICSEARCH_HOST}")
log.info(f"ELASTICSEARCH_INDEX : {ELASTICSEARCH_INDEX}")




log.info("start")

manager = Manager(CONNECTION_STRING , DATABASE , ELASTICSEARCH_HOST , ELASTICSEARCH_INDEX)


manager.start_operations()

