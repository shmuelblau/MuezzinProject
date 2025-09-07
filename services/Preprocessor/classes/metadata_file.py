
import datetime
from pydantic import BaseModel, ConfigDict


class MetadataFile(BaseModel):
    name : str 
    size: int
    creation_time : datetime.datetime

    def get_json(self) -> dict:
        return self.model_dump()

