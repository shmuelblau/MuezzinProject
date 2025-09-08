import io
import gridfs
from classes.logger import Logger , log
from classes.elastic import Elastic
from classes.mongofsDAL import MongoFsDAL
from classes.transcriber import  Transcriber
from classes.elasticDAL import ElasticDAL
from typing import BinaryIO



class Manager:

    @Logger
    def __init__(self , conn_mongo , db_name , elastic_host , elastic_index ) -> None:
        """Receives all the necessary knowledge and produces needed performances"""
        
        self.mongo:MongoFsDAL = MongoFsDAL(conn_mongo , db_name)
        elastic:Elastic = Elastic(elastic_host)
        self.elasticdal = ElasticDAL(elastic)
        self.elastic_index = elastic_index

       

       



    @Logger
    def start_operations(self):

        matadata_list = self.elasticdal.get_all_from_index(self.elastic_index)

        data_with_text = self.get_all_text(matadata_list)
        bulk_list = ElasticDAL.build_update_bulk(self.elastic_index , "text" , data_with_text  )
        self.elasticdal.insert_bulk(bulk_list)


            

    def get_all_text(self ,matadata_list ):
        result:list[dict] = []
        for matadata in matadata_list:
            text = self.get_text_according_to_unique_id(matadata['_source']["unique_id"])
            result.append({"_id" : matadata["_id"] , "text":text } )
        return result

    
    def get_text_according_to_unique_id(self , unique_id) -> str:
        file:gridfs.GridOut = self.mongo.get_one(unique_id)

        text = Transcriber.get_text(file.read())

        return text


            
            

    
            
            

    
    

    

   