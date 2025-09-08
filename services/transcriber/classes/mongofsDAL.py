from pymongo import MongoClient
from pymongo.database import Database
import gridfs
from classes.logger import log , Logger
from classes.singleton import singleton
from typing import BinaryIO



@singleton
class MongoFsDAL:
    """Holds a show of GridFS ​​and allows you to insert and remove files"""
    def __init__(self ,connection_string  , db_name ) -> None:

         self.conn = MongoClient(connection_string)
         db = self.conn[db_name]
         self.fs = gridfs.GridFS(db)

        #  self.files = MongoFiles(self)


    # def __iter__(self):
    #     return self.files
    @property
    def get_conn(self) -> MongoClient:
        
        return self.conn 
    

    
    def insert(self ,file:dict) -> str:
        with open(file["path"], 'rb') as audio_file:
            file_id = self.fs.put(audio_file, filename=file["name"] , unique_id = file["unique_id"] )
        return file_id
    
    
        
    @Logger   
    def get_all(self) -> gridfs.GridOutCursor:
        return self.fs.find()
    
    def get_one(self , unique_id) -> gridfs.GridOut:
        file:gridfs.GridOut = self.fs.find_one({"unique_id" : unique_id})
        return file



# import io
# class MongoFiles():
#     def __init__(self , fs:MongoFsDAL) -> None:
#         self.fs = fs 
#         self.files:list[FsFile] = []
#         self.sent = []


#     def get_files(self) -> list[FsFile]:
        
#         result:list[FsFile] = []
#         files:gridfs.GridOutCursor = self.fs.get_all()
#         for file in files:
#             if file  is not None and file.unique_id not in self.sent:
#                 new_file = FsFile(file. , file.unique_id)

#         return result




#     def __iter__(self):
#         return self.files
    
#     def __next__(self):
#         next = self.files.pop()
#         self.sent.append(next.unique_id)
#         return next.Binary

# from pydantic import BaseModel
# class FsFile(BaseModel):
#     Binary: io.BytesIO 
#     unique_id:str 