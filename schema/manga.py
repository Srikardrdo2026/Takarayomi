from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MangaBase(BaseModel):
    title: str
    author: Optional[str] = None
    description: Optional[str] = None
    status: str
    cover_image: Optional[str] = None
    published_at: Optional[datetime] = None
    genres: Optional[str] = None
    year: Optional[int] = None

class MangaCreate(MangaBase):
    pass

class MangaUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    cover_image: Optional[str] = None
    genres: Optional[str] = None
    status: Optional[str] = None
    published_at: Optional[datetime] = None
    year: Optional[int] = None

class MangaRead(MangaBase):
    id: int

    class Config:
        orm_mode = True
