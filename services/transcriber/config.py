import os 



KAFKA_HOST = os.getenv("KAFKA_HOST" , "kafka")

NEW_TOPIC = os.getenv("NEW_TOPIC" ,"to_classify")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC" ,"to_transcriber")


DATABASE = os.getenv("DATABASE" , "Muezzin")

CONNECTION_STRING = os.getenv("CONNECTION_STRING" )


ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST" , "elasticsearch")

ELASTICSEARCH_INDEX = os.getenv("ELASTICSEARCH_INDEX" , "metadata_muezzin")
ELASTICSEARCH_LOGS_INDEX = os.getenv("ELASTICSEARCH_LOGS_INDEX" , "transcriber_muezzin_logs")


