from classes.logger import Logger , log
from classes.kafka_loader import KafkaLoader
from classes.metadata_provider import MetadataProvider


class Manager:
    
    @Logger
    def __init__(self , host , path , topic) -> None:
        self.kafka_Producer = KafkaLoader(host)
        self.dir_path = path
        self.topic = topic

    @Logger
    def start_operations(self):
        """Extracts the information for all files and pushes it to KAFKA"""

        all_metadata: list[dict] = MetadataProvider.get_all_from_dir(self.dir_path)

        self.kafka_Producer.insert(self.topic ,all_metadata)
        



   