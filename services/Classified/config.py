import os 


PATH_LESS = os.getenv("PATH_LESS" ,"C:/Users/user/Desktop/DATA/Projects/MuezzinProject/services/Classified/data/Less_unfriendly.txt") 
PATH_VERY = os.getenv("PATH_VERY" ,"C:/Users/user/Desktop/DATA/Projects/MuezzinProject/services/Classified/data/Very_unfriendly.txt") 



ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST" , "elasticsearch")

ELASTICSEARCH_INDEX = os.getenv("ELASTICSEARCH_INDEX" , "metadata_muezzin")
ELASTICSEARCH_LOGS_INDEX = os.getenv("ELASTICSEARCH_LOGS_INDEX" , "classified_muezzin_logs")

KAFKA_HOST = os.getenv("KAFKA_HOST" , "kafka")

NEW_TOPIC = os.getenv("NEW_TOPIC" ,"to_transcriber")