import os 

HOST = os.getenv("HOST" , "kafka")

PATH_DIR = os.getenv("PATH_DIR" , "C:/podcasts")

TOPIC_NAME = os.getenv("TOPIC_NAME" ,"Metadata_Muezzin")     



ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST" , "elasticsearch")


ELASTICSEARCH_LOGS_INDEX = os.getenv("ELASTICSEARCH_LOGS_INDEX" , "preprocessor_muezzin_logs")