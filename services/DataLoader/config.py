import os 

KAFKA_HOST = os.getenv("KAFKA_HOST" , "kafka")
TOPIC_NAME = os.getenv("TOPIC_NAME" ,"Metadata_Muezzin")





DATABASE = os.getenv("DATABASE" , "Muezzin")

CONNECTION_STRING = os.getenv("CONNECTION_STRING" )


ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST" , "elasticsearch")
ELASTICSEARCH_INDEX = os.getenv("ELASTICSEARCH_INDEX" , "metadata_muezzin")
