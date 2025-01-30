from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"message":"Hello There!"}

@app.get("/hello")
def hello():
    return {"message": "Hello World!"}

@app.get("/test")
async def another_func():
    return {"message": "Another random route added!"}

@app.get("test_2")
async def another_func():
    return {"message": "Another random route added!"}