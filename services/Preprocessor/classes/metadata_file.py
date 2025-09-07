

from pydantic import BaseModel, ConfigDict


class MetadataFile(BaseModel):
    name : str 
    path : str
    size: int
    creation_time : str


    def get_json(self) -> dict:
        return self.model_dump()

