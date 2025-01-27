from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"message":"Hello There!"}

@app.get("/hello")
def hello():
    return {"message": "Hello World!"}