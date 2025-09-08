from pathlib import Path
import datetime

from classes.metadata_file import MetadataFile

class MetadataProvider:

    @staticmethod
    def get_all_from_dir(path) ->list[dict]:
        """Accepts a path to a folder and returns a detailed description of all the files within it."""

        directory_path = Path(path)
        result : list[dict] = []

        for file in directory_path.iterdir():
            metadata : MetadataFile = MetadataProvider.get_metadata_file(path , file.name)
            metadata_json:dict  = metadata.get_json()
            result.append(metadata_json)

        return result

        



    @staticmethod
    def get_metadata_file(path , file_name)-> MetadataFile:
        
        file_path = Path(path + "/" + file_name)

        stats = file_path.stat()

        name = file_name 
        path = path + "/" + file_name
        size:int = stats.st_size
        creation_time = str(datetime.datetime.fromtimestamp(stats.st_ctime))


        return MetadataFile(name=name , path=path , size=size , creation_time=creation_time)
        
        
