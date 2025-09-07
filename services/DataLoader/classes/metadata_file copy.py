

from pydantic import BaseModel, ConfigDict


class MetadataFile(BaseModel):
    name : str 
    path : str
    size: int
    creation_time : str


    def get_json(self) -> dict:
        return self.model_dump()
    
    @staticmethod
    def from_json(data:dict) :
        return MetadataFile(name=data["name"] , path=data["path"] , size=data["size"] , creation_time=data["creation_time"])


