import os
import time
import uuid
from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/ping")
async def ping():
    time.sleep(3)
    return {"message": str(uuid.uuid4()), "status": "OK"}


@app.post("/upload-file")
async def upload_file(file: UploadFile):
    file_data = b""
    file_name = str(uuid.uuid4())
    for chunk in file.file:
        file_data += chunk

    with open(f"received/{file_name}.bin", "wb") as _file:
        _file.write(file_data)

    os.remove(f"received/{file_name}.bin")

    return {"message": "upload file", "status": "OK"}
