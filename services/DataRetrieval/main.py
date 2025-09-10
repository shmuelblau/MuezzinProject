from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from classes.manager import Manager
from config import *
import time

from Models.ThreatLevelRequest import ThreatLevelRequest

app = FastAPI()

manager = Manager(ELASTICSEARCH_HOST , ELASTICSEARCH_INDEX)


@app.post("/get_by_threat_level")
def get_by_threat_level(request:ThreatLevelRequest):

    result:list[dict] = manager.get_by_threat_level(request)
    return JSONResponse(content={} , status_code=200)


@app.get("/get_all_info")
def get_all_info():

    result:dict = manager.get_all_info()
    return JSONResponse(content={} , status_code=200)





