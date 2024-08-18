from fastapi import FastAPI
import uvicorn


# client -> uvicorn -> web framework (FastAPI)
app = FastAPI()

@app.get("/")
async def home():
    return {"msg": "Hello World"}

# Run the following command in shell to start server (if not run .py directly)
# uvicorn simple_fastapi:app --reload

# Default port is 8000

if __name__ == "__main__":
    uvicorn.run(
        app="simple_fastapi:app",
        host="127.0.0.1",
        port=8080,
        reload=True
    )
