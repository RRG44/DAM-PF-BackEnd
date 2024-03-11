import ExifUtility as exif
import VirusTotalAPIConnection as vt
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# bash: uvicorn main:app --reload

app = FastAPI()

@app.get("/scan_url/{urlBase64}")
def getUrlInfor(urlBase64: str):
  return vt.fetchVirusTotal(urlBase64)

@app.get("/scan_url_test/{urlBase64}")
def getUrlInfor(urlBase64: str):
  return vt.fetchVirusTotal(urlBase64)

class ImageRequest(BaseModel):
  name: str
  image: str

@app.get("/clean_exif/")
def cleanExifData(data: ImageRequest):
  name: data.name
  image: data.image
  return {"message" : "Hello!"}
