import time
from elastic_transport import ObjectApiResponse
from elasticsearch import Elasticsearch
from classes.logger import Logger , get_logger
from classes.singleton import singleton

log = get_logger()


@singleton
class Elastic():
    
  
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

