from pydantic import BaseModel
from typing import Optional

class PageRead(BaseModel):
    id: int
    chapter_id: int
    page_number: int
    image_url: str
    local_path: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    
    class Config:
        orm_mode = True
    
class PageCreate(BaseModel):
    chapter_id: int
    page_number: int
    image_url: str
    local_path: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None