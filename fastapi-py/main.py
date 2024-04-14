from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.get("/ping")
async def ping():
    return {"message": "pong", "status": "OK"}


@app.post("/upload-file")
async def upload_file(file: UploadFile):
    for chunk in file.file:
        print(chunk)
    return {"message": "upload file", "status": "OK"}
