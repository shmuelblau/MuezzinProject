
from classes.singleton import singleton
from kafka import KafkaConsumer
import json

@singleton
class KafkaReader:

    def __init__(self ,kafka_host,  topic) -> None:
        self.conn = KafkaConsumer(
            topic,
            bootstrap_servers=f'{kafka_host}:9092',
            auto_offset_reset='earliest',
            group_id = topic,
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                       
        )
    @property   
    def get_conn(self) -> KafkaConsumer:
    
            return self.conn 
