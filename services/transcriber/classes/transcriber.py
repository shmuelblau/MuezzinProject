from faster_whisper import WhisperModel
from classes.mongofsDAL import MongoFsDAL
from classes.singleton import singleton
from classes.logger import Logger
from classes.elasticDAL import ElasticDAL
from typing import BinaryIO
@singleton
class Transcriber:
      
      def __init__(self , mongo:MongoFsDAL , elastic:ElasticDAL , elastic_index:str) -> None:
            self.mongo:MongoFsDAL = mongo
            self.elastic:ElasticDAL = elastic
            self.elastic_index:str = elastic_index
            self.model = WhisperModel("base")



      
      @Logger(log_start=False)
      def get_text(self , file:BinaryIO)->str:
            segments, info = self.model.transcribe(file)

            text = ".".join([s.text for s in segments])
            return text

      


      
      
      


