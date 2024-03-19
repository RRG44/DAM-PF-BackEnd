import os
import tempfile
import ExifUtility as exif
import VirusTotalAPIConnection as vt
from typing import Union
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.responses import JSONResponse, FileResponse
import mimetypes
import base64

# bash: uvicorn main:app --reload

app = FastAPI()

@app.get("/scan_url/{urlBase64}")
async def getUrlInfo(urlBase64: str):
  return vt.fetchVirusTotal(urlBase64)

@app.get("/scan_url_test/{urlBase64}")
async def getUrlInfo(urlBase64: str):
  return vt.fetchVirusTotal(urlBase64)

# class ImageRequest(BaseModel):
#   name: str
#   image: str

# @app.get("/clean_exif/")
# async def cleanExifData(data: ImageRequest):
#   name: data.name
#   image: data.image
#   return {"message" : "Hello!"}

@app.post("/clean_exif/")
async def upload_file(name: str, image: UploadFile = File(...)):
    try:
        
        with tempfile.TemporaryDirectory() as tmp_dir:

          file_name = 'clean_exif_'+name
          path_to_file = os.path.join(tmp_dir, file_name)

          contents = await image.read()
          
          with open(path_to_file, "wb") as f:
            f.write(contents)

          # TODO: image processsing

          exif_data = exif.readExif(path_to_file)

          exif.deleteExif(path_to_file)

          image_data = open(path_to_file, "rb").read()

          image_data_b64 = base64.b64encode(image_data).decode("utf-8")

          return JSONResponse(content={"name": file_name, "image": image_data_b64, "exif": exif_data})
          # return JSONResponse(content={"name": name, "image": contents, "exif" : exif_data})
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
