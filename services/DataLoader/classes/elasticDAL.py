from elastic_transport import ObjectApiResponse
from elasticsearch import Elasticsearch
from classes.elastic import Elastic
from classes.logger import Logger
from classes.singleton import singleton


@singleton
class ElasticDAL:
# ----------------------------------------------------------------------------

    def __init__(self , elastic:Elastic) -> None:
       self.conn:Elasticsearch = elastic.get_conn

# ----------------------------------------------------------------------------

    @property
    def get_conn(self) -> Elasticsearch:
        return self.conn
    
# ----------------------------------------------------------------------------
    @Logger
    def get_all_from_index(self , index)-> list[dict]:
        result = self.search( index ,{"query": {"match_all": {}}})
        return result
# ----------------------------------------------------------------------------

    @Logger
    def search(self , index , query)-> list[dict]:
        result = self.conn.search(index=index , body= query , size=10000)
        return result['hits']['hits']
# ----------------------------------------------------------------------------
    @Logger(log_start=False)
    def insert(self , index , data:dict) -> ObjectApiResponse:
        result = self.conn.index(index= index ,document= data)
        self.refresh()
        return result
    
    @Logger(log_start=False)
    def refresh(self ):
        self.conn.indices.refresh()