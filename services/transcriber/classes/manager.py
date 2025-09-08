from classes.logger import Logger , log
from classes.elastic import Elastic
from classes.mongofsDAL import MongoFsDAL
from classes.transcriber import  Transcriber
from classes.elasticDAL import ElasticDAL




class Manager:

    @Logger
    def __init__(self , conn_mongo , db_name , elastic_host , elastic_index ) -> None:
        """Receives all the necessary knowledge and produces needed performances"""
        
        self.mongo:MongoFsDAL = MongoFsDAL(conn_mongo , db_name)
        elastic:Elastic = Elastic(elastic_host)
        self.elasticdal = ElasticDAL(elastic)

        self.transcriber = Transcriber(self.mongo , self.elasticdal ,elastic_index)
        
       



    @Logger
    def start_operations(self):

        pass
            
            

    
            
            

    
    

    

   