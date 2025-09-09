import os 

KAFKA_HOST = os.getenv("KAFKA_HOST" , "kafka")
TOPIC_NAME = os.getenv("TOPIC_NAME" ,"Metadata_Muezzin")
NEW_TOPIC = os.getenv("NEW_TOPIC" ,"to_transcriber")






DATABASE = os.getenv("DATABASE" , "Muezzin")

CONNECTION_STRING = os.getenv("CONNECTION_STRING" )


ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST" , "elasticsearch")

ELASTICSEARCH_INDEX = os.getenv("ELASTICSEARCH_INDEX" , "metadata_muezzin")
ELASTICSEARCH_LOGS_INDEX = os.getenv("ELASTICSEARCH_LOGS_INDEX" , "dataloader_muezzin_logs")