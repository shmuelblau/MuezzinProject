from kafka import KafkaProducer
from classes.logger import get_logger
import json
log = get_logger()
class KafkaLoader:

    def __init__(self , host) -> None:
        self.producer = KafkaProducer(
                        bootstrap_servers = f'{host}:9092',
                        value_serializer=lambda v: json.dumps(v).encode('utf-8')
                    )
        

    
    def insert(self ,topic , data:list[dict]):
        try:
            log.info(f"try insert data topic:{topic}  len:{len(data)}")
            for i in data:
                
                self.producer.send(topic , i )

            self.producer.flush()
            log.info("success insert")

        except Exception as e:
            log.info("failed insert data to kafka")
            log.info(f"error:{e}")




