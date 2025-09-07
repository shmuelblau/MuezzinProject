
from classes.metadata_file import MetadataFile
from classes.elastic import Elastic
from classes.mongoDAL import mongoDAL


class DataLoader:
      def __init__(self , mongo:mongoDAL , elastic:Elastic , elastic_index:str) -> None:
            self.mongo = mongo
            self.elastic = elastic
            self.elastic_index = elastic_index

      def send_file(self , data:dict):
            unique_id = DataLoader.get_hash(data)
            data["unique_id"] = unique_id
            self.elastic.insert(self.elastic_index , data)

            
            self.mongo.insert(data) 

      


      @staticmethod
      def get_hash(data:dict) -> str:
          return str(hash(data["name"] ))
      


