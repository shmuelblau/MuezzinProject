import os 

KAFKA_HOST = os.getenv("KAFKA_HOST" , "kafka")
TOPIC_NAME = os.getenv("TOPIC_NAME" ,"Metadata_Muezzin")





DATABASE = os.getenv("DATABASE" , "Muezzin")
COLLECTION = os.getenv("COLLECTION" , "files_muezzin")
CONNECTION_STRING = os.getenv("CONNECTION_STRING" ,"mongodb://shmuel:1234@mongo:27017/TextFeature?authSource=admin")


ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST" , "elasticsearch")
ELASTICSEARCH_INDEX = os.getenv("ELASTICSEARCH_INDEX" , "Metadata_Muezzin")
