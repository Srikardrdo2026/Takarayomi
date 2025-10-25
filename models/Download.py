from sqlalchemy import Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from datetime import datetime

class Download(Base):
    __tablename__ = 'downloads'
    
    #Attributes
    id:Mapped[int] = mapped_column(primary_key=True)
    chapter_id:Mapped[int] = mapped_column(ForeignKey('chapter.id'), nullable=False)
    file_path:Mapped[str] = mapped_column(Text, nullable=False)
    download_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    is_complete:Mapped[bool] = mapped_column(default=False, nullable=False)
    
    #Relationships
    chapter = relationship("Chapter", back_populates="downloads")