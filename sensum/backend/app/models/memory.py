from pydantic import BaseModel
from typing import Optional
from datetime import date

class MemoryCreate(BaseModel):
    user_id: int
    date: date
    text: str
    emote: Optional[str] = None

class MemoryResponse(BaseModel):
    date: date
    text: str
    emote: Optional[str]

class MemoryUpdate(BaseModel):
    text: Optional[str] = None
    emote: Optional[str] = None

class MemoryDelete(BaseModel):
    id: int
