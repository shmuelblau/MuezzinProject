from classes.logger import Logger , log
from classes.elastic import Elastic

from classes.elasticDAL import ElasticDAL




class Manager:

    @Logger
    def __init__(self , elastic_host , elastic_index ) -> None:
        """Receives all the necessary knowledge and produces needed performances"""

        elastic:Elastic = Elastic(elastic_host)
        self.elasticdal:ElasticDAL = ElasticDAL(elastic)
        self.elastic_index = elastic_index
        
       



    

            
        
            
            

    
            
            

    
    

    

   