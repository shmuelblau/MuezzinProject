from classes.logger import Logger , log
from classes.elastic import Elastic
from classes.mongofsDAL import MongoFsDAL
from classes.transcriber import  Transcriber
from classes.elasticDAL import ElasticDAL
from classes.kafka_loader  import KafkaLoader

from classes.kafka_reader import KafkaReader



class Manager:

    @Logger
    def __init__(self , conn_mongo , db_name , elastic_host , elastic_index ,kafka_host , kafka_topic , new_topic ) -> None:
        """Receives all the necessary knowledge and produces needed performances"""
        
        self.mongo:MongoFsDAL = MongoFsDAL(conn_mongo , db_name)
        elastic:Elastic = Elastic(elastic_host)
        self.elasticdal:ElasticDAL = ElasticDAL(elastic)
        self.elastic_index = elastic_index
        self.kafkareader:KafkaReader = KafkaReader(kafka_host=kafka_host , topic=kafka_topic)
        self.kafkaloader = KafkaLoader(kafka_host)
        self.new_topic = new_topic

       



    @Logger
    def start_operations(self):

        for new_file in self.kafkareader.get_conn:
            unique_id = new_file.value["unique_id"]
            text = self.get_text_according_to_unique_id(unique_id)
            self.insert_text_to_elastic(unique_id=unique_id , text=text)

            self.kafkaloader.insert( self.new_topic, [{"unique_id":unique_id}])


    @Logger(log_start=False)
    def get_text_according_to_unique_id(self , unique_id) -> str:
        file = self.mongo.get_one(unique_id)
        by_file:bytes = file.read()
        text = Transcriber.get_text(by_file)

        return text

    @Logger(log_start=False)
    def insert_text_to_elastic(self , unique_id , text):

        elastic_id = self.elasticdal.get_id_by_field(self.elastic_index , "unique_id" , unique_id)
        bulk:list = self.elasticdal.build_update_bulk(index = self.elastic_index , field_name= "text" , data=[{"_id" :elastic_id , "text" : text }] )
        self.elasticdal.insert_bulk(bulk)

            
        
            
            

    
            
            

    
    

    

   