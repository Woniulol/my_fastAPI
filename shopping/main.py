from fastapi import FastAPI
import uvicorn

from apps.app_01.urls import shop
from apps.app_02.urls import user

app = FastAPI()

app.include_router(shop, prefix="/shop", tags=["Shopping Center"])
app.include_router(user, prefix="/user", tags=["User Center"])

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="127.0.0.1",
        port=8080,
        reload=True
    )