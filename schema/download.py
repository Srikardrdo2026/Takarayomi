from pydantic import BaseModel
from datetime import datetime

class DownloadRead(BaseModel):
    id: int
    chapter_id: int
    file_path: str
    download_at: datetime
    is_complete: bool

    class Config:
        orm_mode = True

class DownloadCreate(BaseModel):
    chapter_id: int
    file_path: str
    is_complete: bool = False
