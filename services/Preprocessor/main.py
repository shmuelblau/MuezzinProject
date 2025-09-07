
from classes.manager import Manager
from config import *
from classes.logger import get_logger
import time

log = get_logger()



time.sleep(25)
log.info("start")

manager = Manager(HOST , PATH_DIR , TOPIC_NAME)

manager.start_operations()