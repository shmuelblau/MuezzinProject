from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from classes.manager import Manager
from config import *
import time

app = FastAPI()

manager = Manager(ELASTICSEARCH_HOST , ELASTICSEARCH_INDEX)


@app.get("/download")
def download_file():
    return JSONResponse(content={} , status_code=200)





