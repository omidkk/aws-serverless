from fastapi import APIRouter
from typing import List
import re

router = APIRouter()


@router.post("/af-v1")
async def array_flatten_v1(array: List):
    num_array = re.split('\[|\]|\(|\)|,', str(array))
    return [float(x) for x in num_array if len(x.strip())>0]

@router.post("/af-v2")
async def array_flatten_v2(array: List):
    arr = []
    array_flatten(array,arr)
    return arr


def array_flatten(array: List, arr: List):
    for x in array:
        if isinstance(x, List):
            array_flatten(x,arr)
        else:
            arr.append(x)
