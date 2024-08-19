from typing import List
from fastapi import APIRouter, File, UploadFile


app05 = APIRouter()

@app05.post("/file")
async def get_file(file: bytes = File()):
    # for small file upload
    print(file)
    return {"file": "file"}

@app05.post("/files")
async def get_files(files: List[bytes] = File()):
    # for small files upload
    print(files)
    return {"files": "files"}

@app05.post("/uploadFile")
async def get_large_file(file: UploadFile):
    # file is no longer the bytes but rather a file object
    print("file", file)
    for line in file.file:
        ...
    return {"file": file.filename}