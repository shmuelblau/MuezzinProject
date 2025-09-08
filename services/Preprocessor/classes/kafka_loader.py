from kafka import KafkaProducer
from classes.logger import get_logger
import json
from classes.singleton import singleton
log = get_logger()

@singleton
class KafkaLoader:

    def __init__(self , host) -> None:
        self.producer = KafkaProducer(
                        bootstrap_servers = f'{host}:9092',
                        value_serializer=lambda v: v.encode('utf-8')
                    )
        

    
    def insert(self ,topic , data:list[dict]):
        try:
            log.info(f"try insert data topic:{topic}  len:{len(data)}")
            for line in data:
                
                line = json.dumps(line)
                self.producer.send(topic , line)

            self.producer.flush()
            log.info("success insert")

        except Exception as e:
            log.info("failed insert data to kafka")
            log.info(f"error:{e}")




