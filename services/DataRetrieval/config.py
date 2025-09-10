import os 

ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST" , "elasticsearch")

ELASTICSEARCH_INDEX = os.getenv("ELASTICSEARCH_INDEX" , "metadata_muezzin")
ELASTICSEARCH_LOGS_INDEX = os.getenv("ELASTICSEARCH_LOGS_INDEX" , "dataretrieval_muezzin_logs")


