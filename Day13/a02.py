from fastapi import FastAPI
from pydantic import BaseModel
from calculator import add, subtract

#The Swagger UI will be available at http://127.0.0.1:8000/docs.
#pip install fastapi uvicorn



# FastAPI app instance
app = FastAPI()

'''
The code you provided defines a Pydantic model class called Numbers,
 which is a subclass of BaseModel. Pydantic is a data validation and settings 
 management library in Python, which uses Python's type annotations to
   validate data.
'''

# Pydantic model to parse input data
class Numbers(BaseModel):
    a: int
    b: int


'''
input in post request body...

{
  "a": 0,
  "b": 0
}

'''



# Route to add two numbers
@app.post("/add")
def perform_addition(numbers: Numbers):
    result = add(numbers.a, numbers.b)
    return {"result": result}

# Route to subtract two numbers
@app.post("/subtract")
def perform_subtraction(numbers: Numbers):
    result = subtract(numbers.a, numbers.b)
    return {"result": result}


