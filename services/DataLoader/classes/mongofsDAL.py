from pymongo import MongoClient
from pymongo.database import Database
import gridfs
from classes.logger import log , Logger
from classes.singleton import singleton


@singleton
class MongoFsDAL:
    """Holds a show of GridFS ​​and allows you to insert and remove files"""
    def __init__(self ,connection_string  , db_name ) -> None:

         self.conn = MongoClient(connection_string)
         db = self.conn[db_name]
         self.fs = gridfs.GridFS(db)
        
    
    @property
    def get_conn(self) -> MongoClient:
        
        return self.conn 
    

    
    def insert(self ,file:dict) -> str:
        with open(file["path"], 'rb') as audio_file:
            file_id = self.fs.put(audio_file, filename=file["name"] , unique_id = file["unique_id"] )
        return file_id
    @Logger   
    def get_all(self):
        return self.fs.list()






