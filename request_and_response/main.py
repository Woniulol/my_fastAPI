from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from apps.app01_path_var import app01
from apps.app02_query_var import app02
from apps.app03_request_body import app03
from apps.app04_form import app04
from apps.app05 import app05
from apps.app06 import app06
from apps.app07 import app07


app = FastAPI()

app.mount("/statics", StaticFiles(directory="statics"))

app.include_router(app01, tags=["path variable"])
app.include_router(app02, tags=["inquiry variable"])
app.include_router(app03, tags=["request body"])
app.include_router(app04, tags=["request body form"])
app.include_router(app05, tags=["file upload"])
app.include_router(app06, tags=["request object"])
app.include_router(app07, tags=["response module"])

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="127.0.0.1",
        port=8080,
        reload=True
    )