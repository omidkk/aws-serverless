from fastapi import APIRouter
from typing import List
import re
from pydantic import BaseModel

router = APIRouter()


class Input(BaseModel):
    input: List

@router.post("/af-v1")
async def array_flatten_v1(input: Input):
    num_array = re.split('\[|\]|\(|\)|,', str(input.input))
    return {"output": [float(x) for x in num_array if len(x.strip())>0]}

@router.post("/af-v2")
async def array_flatten_v2(input: Input):
    arr = []
    array_flatten(input.input,arr)
    return {"output": arr}


def array_flatten(array: List, arr: List):
    for x in array:
        if isinstance(x, List):
            array_flatten(x,arr)
        else:
            arr.append(x)
