
from pydantic import BaseModel
from typing import List

class CaptureRequest(BaseModel):
    url: str

class CaptureList(BaseModel):
    captures: List[CaptureRequest]
