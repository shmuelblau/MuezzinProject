
from classes.manager import Manager
from config import *
from classes.logger import get_logger
import time

log = get_logger()

log.info(f"HOST : {HOST}")
log.info(f"PATH_DIR : {PATH_DIR}")
log.info(f"TOPIC_NAME : {TOPIC_NAME}")


time.sleep(25)
log.info("start")

manager = Manager(HOST , PATH_DIR , TOPIC_NAME)

manager.start_operations()