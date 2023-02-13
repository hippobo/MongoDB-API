
from fastapi import FastAPI
from pydantic import BaseModel

import pymongo
from db_requests import DB_connection
print("HERE")

app = FastAPI()

class Item(BaseModel):
    _id : str
    titleId: str
    ordering: int
    title: str
    region: str
    language: str
    types: str
    attributes: str
    isOriginalTitle: str

@app.get("/api/id={Id}")
def get_title(Id: str):

    return DB_connection(("IMDB")).get_document_by_id("titles", Id)

@app.get("/api/random")
def return_random():
    return DB_connection(("IMDB")).get_random_document("titles")



print("here")
import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)

