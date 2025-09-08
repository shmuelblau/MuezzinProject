
from classes.metadata_file import MetadataFile
from classes.elastic import Elastic
from classes.mongoDAL import MongoFsDAL
from classes.singleton import singleton
from classes.logger import Logger
from classes.elasticDAL import ElasticDAL

@singleton
class DataLoader:
      def __init__(self , mongo:MongoFsDAL , elastic:ElasticDAL , elastic_index:str) -> None:
            self.mongo:MongoFsDAL = mongo
            self.elastic:ElasticDAL = elastic
            self.elastic_index:str = elastic_index


      @Logger(log_start=False)
      def send_file(self , data:dict):
            unique_id = self.get_hash(data)
            data["unique_id"] = unique_id
            self.elastic.insert(self.elastic_index , data)

            
            self.mongo.insert(data) 

      


      
      def get_hash(self , data:dict) -> str:
          return str(hash(data["name"] ))
      


