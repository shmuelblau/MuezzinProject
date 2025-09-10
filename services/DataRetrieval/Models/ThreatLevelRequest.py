from pydantic import BaseModel 
from typing import Literal

statuses = Literal["none" ,"medium" , "high" , "all"]

class ThreatLevelRequest(BaseModel):
    status:statuses
