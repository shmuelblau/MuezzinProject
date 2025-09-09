import time
from elastic_transport import ObjectApiResponse
from elasticsearch import Elasticsearch
from classes.logger import Logger , log
from classes.singleton import singleton




@singleton
class Elastic():
    """Basic connection to elastic"""
    
  
    def __init__(self , host , port = 9200) -> None:
        self.conn: Elasticsearch = self._set_conn( host , port = 9200)
        log.info(f"ping : {self.conn.ping()}")
        
    
    
    @Logger
    def _set_conn(self , host , port = 9200):
        self.conn: Elasticsearch = Elasticsearch(f'http://{host}:{port}')
        self.conn.ping()
        return self.conn

    
    @property
    def get_conn(self) -> Elasticsearch:
        return self.conn

