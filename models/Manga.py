from sqlalchemy import String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from datetime import datetime

class Manga(Base):
    __tablename__ = "manga"
    
    #Attributes
    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(300), index=True, nullable=False)
    author:Mapped[str] = mapped_column(String(100), nullable=True)
    description:Mapped[str] = mapped_column(Text, nullable=True)
    cover_image:Mapped[str] = mapped_column(String(500), nullable=True)
    status:Mapped[str] = mapped_column(String(50), default="ongoing", nullable=False)
    published_at:Mapped[datetime] = mapped_column(DateTime, nullable=True)
    last_updated:Mapped[datetime] = mapped_column(DateTime, nullable=True)
    genres:Mapped[str] = mapped_column(Text, nullable=True)
    year:Mapped[int] = mapped_column(nullable=True)

    #Relationships
    chapters = relationship("Chapter", back_populates="manga", cascade="all, delete-orphan")
    favorites = relationship("Favorite", back_populates="manga", cascade="all, delete-orphan")