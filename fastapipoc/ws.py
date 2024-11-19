from fastapi import FastAPI 
from logic import Logic 
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/run")
# async def func():
#     a = Logic()
#     result = a.rs()
#     return result

@app.get("/get")
async def func(n):
    a = Logic()
    result = a.nextnumber(int(n))
    return {"result": result}

