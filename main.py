from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Multiply_param(BaseModel):
    param1: int
    param2: int

@app.get("/addition")
def addition(param1: int, param2: int):
    return {"sum": param1 + param2}

@app.post("/multiply")
def multiply(params: Multiply_param):
    result = params.param1 * params.param2
    return {"result": result}


@app.post("/square/{param}")
def square(param: int):
    return {"param": param**2 }


