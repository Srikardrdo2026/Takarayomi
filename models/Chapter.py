from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from datetime import datetime

class Chapter(Base):
    __tablename__ = "chapter"
    
    #Attributes
    id:Mapped[int] = mapped_column(primary_key=True)
    manga_id:Mapped[int] = mapped_column(ForeignKey("manga.id"), nullable=False)
    title:Mapped[str] = mapped_column(String(300), nullable=False)
    chapter_number:Mapped[float] = mapped_column(nullable=False)
    volume:Mapped[int] = mapped_column(nullable=True)
    release_date:Mapped[datetime] = mapped_column(DateTime, nullable=True)
    url:Mapped[str] = mapped_column(String(500), nullable=False)
    last_uploaded:Mapped[datetime] = mapped_column(DateTime, nullable=True)
    
    #Relationships
    manga = relationship("Manga", back_populates="chapters")
    pages = relationship("Page", back_populates="chapter", cascade="all, delete-orphan")
    downloads = relationship("Download", back_populates="chapter", cascade="all, delete-orphan")
