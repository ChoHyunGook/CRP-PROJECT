mport datetime
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os
from spec import Spec

app = FastAPI()
origins = [ "http://localhost:8000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message":"Hello World"}    

@app.get("/now")
async def now():
    return {"now":datetime.datetime.now().strftime('%Y-%m-%d')}


@app.post("/files")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/files/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    UPLOAD_DIRECTORY = "./"
    for file in files:
        contents = await file.read()
        with open(os.path.join(UPLOAD_DIRECTORY, file.filename), "wb") as fp:
            fp.write(contents)
        print(file.filename)
    fname= [file.filename for file in files][0]
    return Spec.service(filename=fname)

##################
# fastapi/spec.py
##################

from pydantic import BaseModel
from item import Item
from color import Color


class Filename(BaseModel):
    name: str

class Spec:
    @staticmethod
    def item(filename : Filename):
        print(f'{filename}')
        item = Item(filename.name).find_item()
        return item   

    @staticmethod
    def color(filename: Filename):
        print(f'{filename}')
        color = Color(filename.name).discrimination_color()
        return color

    @staticmethod
    def service(filename: Filename):
        print(f'{filename}')


        item = Item(filename).find_item()
        color = Color(filename).discrimination_color()
        return {"item": item, "color":color} 