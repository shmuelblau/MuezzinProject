from classes.logger import Logger , get_logger
from classes.elastic import Elastic
from classes.kafka_reader import KafkaReader
from classes.mongoDAL import MongoFsDAL
from classes.data_loader import DataLoader
from classes.elasticDAL import ElasticDAL


log = get_logger()

class Manager:

    @Logger
    def __init__(self , kafka_host , topic_name  , conn_mongo , db_name , elastic_host , elastic_index ) -> None:
        self.set_kafka(kafka_host , topic_name)

        mongo:MongoFsDAL = MongoFsDAL(conn_mongo , db_name)
        elastic:Elastic = Elastic(elastic_host)
        elasticdal = ElasticDAL(elastic)

        self.DataLoader = DataLoader(mongo , elasticdal , elastic_index)

        self.elastic_index = elastic_index

    @Logger
    def start_operations(self):

        for file in self.topic:
            self.DataLoader.send_file(file.value)
            
            

    def set_kafka(self , kafka_host , topic_name ) -> None:
        self.topic = KafkaReader(kafka_host=kafka_host , topic=topic_name).get_conn
    

    

   