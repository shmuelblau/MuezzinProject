import io
import gridfs
from classes.logger import Logger , log
from classes.elastic import Elastic

from classes.elasticDAL import ElasticDAL
from typing import BinaryIO
from classes.classified import Classified
from classes.kafka_reader import KafkaReader


class Manager:

    @Logger
    def __init__(self , elastic_host , elastic_index ,kafka_host ,  new_topic) -> None:
        elastic:Elastic = Elastic(elastic_host)
        self.elasticdal:ElasticDAL = ElasticDAL(elastic)
        self.elastic_index = elastic_index
        self.kafkareader:KafkaReader = KafkaReader(kafka_host=kafka_host , topic=new_topic)
        
        self.new_topic = new_topic

       

       



    @Logger
    def start_operations(self):
        for new_file in self.kafkareader.get_conn:
            unique_id = new_file.value["unique_id"]
            doc = self.elasticdal.search(self.elastic_index , {})
            text = doc[0]["_source"]["text"]
            id = doc[0]["_id"]
            all_farams:dict = Classified.get_all_farams(text)

            self.add_to_elastic(self.elastic_index , id , all_farams)


            
        

    

    @Logger       
    def add_to_elastic(self , index , id , data:dict):
        pass
            
            

    
            
            

    
    

    

   