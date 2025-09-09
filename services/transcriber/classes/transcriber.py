from faster_whisper import WhisperModel
from classes.mongofsDAL import MongoFsDAL
from classes.singleton import singleton
from classes.logger import Logger
from classes.elasticDAL import ElasticDAL
from typing import BinaryIO
import io

class Transcriber:
      
      model = WhisperModel("base")

      @staticmethod
      def get_text( file:bytes)->str:
            segments, info = Transcriber.model.transcribe(io.BytesIO(file))

            text = ".".join([s.text for s in segments])
            return text

      


      
      
      


