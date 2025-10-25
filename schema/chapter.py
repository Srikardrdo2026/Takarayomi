from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ChapterBase(BaseModel):
    manga_id: int
    title: str
    chapter_number: float
    volume: Optional[int] = None
    release_date: Optional[datetime] = None
    url: str
    
class ChapterCreate(ChapterBase):
    pass

class ChapterRead(ChapterBase):
    id: int
    last_uploaded: datetime
    
    class Config:
        orm_mode = True