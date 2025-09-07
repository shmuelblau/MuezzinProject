from elastic_transport import ObjectApiResponse
from elasticsearch import Elasticsearch
from classes.logger import Logger , get_logger

log = get_logger()
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
    
    

    @Logger(log_start=False)
    def insert(self , index , data:dict) -> ObjectApiResponse:
        result = self.conn.index(index= index ,document= data)
        self.refresh()
        return result
    
    @Logger(log_start=False)
    def refresh(self ):
        self.conn.indices.refresh()