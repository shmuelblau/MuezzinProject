from classes.logger import Logger , log
from classes.elastic import Elastic
from classes.kafka_reader import KafkaReader
from classes.mongofsDAL import MongoFsDAL
from classes.data_loader import DataLoader
from classes.elasticDAL import ElasticDAL
from classes.kafka_loader import KafkaLoader




class Manager:

    @Logger
    def __init__(self , kafka_host , topic_name ,new_topic , conn_mongo , db_name , elastic_host , elastic_index ) -> None:
        """Receives all the necessary knowledge and produces needed performances"""
        self.set_kafka(kafka_host , topic_name)

        mongo:MongoFsDAL = MongoFsDAL(conn_mongo , db_name)
        elastic:Elastic = Elastic(elastic_host)
        elasticdal = ElasticDAL(elastic)
        kafkaloader = KafkaLoader(kafka_host)
        self.DataLoader = DataLoader(mongo , elasticdal , elastic_index ,kafkaloader,new_topic)

        self.elastic_index = elastic_index

    @Logger
    def start_operations(self):

        for file in self.topic:
            self.DataLoader.send_file(file.value)
            
            

    def set_kafka(self , kafka_host , topic_name ) -> None:
        self.topic = KafkaReader(kafka_host=kafka_host , topic=topic_name).get_conn
    

    

   