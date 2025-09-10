from classes.logger import Logger , log
from classes.elastic import Elastic

from classes.elasticDAL import ElasticDAL
from Models.ThreatLevelRequest import ThreatLevelRequest




class Manager:

    @Logger
    def __init__(self , elastic_host , elastic_index ) -> None:
        """Receives all the necessary knowledge and produces needed performances"""



        elastic:Elastic = Elastic(elastic_host)
        self.elasticdal:ElasticDAL = ElasticDAL(elastic)
        self.elastic_index = elastic_index
        
       
    @Logger
    def get_by_threat_level(self , request:ThreatLevelRequest)-> list[dict]:

        if request.status == "all":
            result = self.elasticdal.get_all_from_index(self.elastic_index)
        else:
            result = self.elasticdal.get_all_by_field(self.elastic_index ,"bds_threat_level" , request.status )

        result = [doc['_source'] for doc in result]

        return result
    
    def get_all_info(self) -> dict:

        none_list = self.elasticdal.get_all_by_field(self.elastic_index ,"bds_threat_level" , "none" )
        medium_list = self.elasticdal.get_all_by_field(self.elastic_index ,"bds_threat_level" , "medium" )
        high_list = self.elasticdal.get_all_by_field(self.elastic_index ,"bds_threat_level" , "high" )

        len_none = len(none_list)
        len_bds = len(medium_list) + len(high_list)

        percentage = sum([int(doc['_source']["bds_percent"] )for doc in high_list + medium_list  ])
        average = percentage // ( len_none + len_bds)
        
        return {
            "bds_threat_level" : {"none" : len(none_list)  ,"medium": len(medium_list) , "high": len(high_list) },
            "is_bds" : {"true" : len_bds , "false":len_none},
            "average" : average

        }





    

            
        
            
            

    
            
            

    
    

    

   