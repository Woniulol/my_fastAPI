from fastapi import FastAPI
import uvicorn

from apps.app01_path_var import app01
from apps.app02_query_var import app02
from apps.app03_request_body import app03


app = FastAPI()
app.include_router(app01, tags=["path variable"])
app.include_router(app02, tags=["inquiry variable"])
app.include_router(app03, tags=["request body"])

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="127.0.0.1",
        port=8080,
        reload=True
    )