from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from datetime import datetime

class Favorite(Base):
    __tablename__ = 'favorites'
    
    #Attributes
    id:Mapped[int] = mapped_column(primary_key=True)
    manga_id:Mapped[int] = mapped_column(ForeignKey("manga.id"), nullable=False)
    status:Mapped[str] = mapped_column(String(50), default="ongoing", nullable=False)
    added_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    last_read_chapter:Mapped[int] = mapped_column(ForeignKey("chapter.id"), nullable=True)
    
    #Relationships
    manga = relationship("Manga", back_populates="favorites")
    last_read_chapter_rel = relationship("Chapter")