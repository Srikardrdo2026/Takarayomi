from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FavoriteResponse(BaseModel):
    id: int
    manga_id: int
    status: str
    added_at: datetime
    last_read_chapter: Optional[int] = None

    class Config:
        orm_mode = True

class FavoriteCreate(BaseModel):
    manga_id: int
    status: Optional[str] = "ongoing"
    last_read_chapter: Optional[int] = None
