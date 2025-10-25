from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Page(Base):
    __tablename__ = "page"
    
    #Attributes
    id:Mapped[int] = mapped_column(primary_key=True)
    chapter_id:Mapped[int] = mapped_column(ForeignKey("chapter.id"), nullable=False)
    page_number:Mapped[int] = mapped_column(nullable=False)
    image_url:Mapped[str] = mapped_column(String(500), nullable=False)
    local_path:Mapped[str] = mapped_column(String(500), nullable=True)
    width:Mapped[int] = mapped_column(nullable=True)
    height:Mapped[int] = mapped_column(nullable=True)
    
    #Relationships
    chapter = relationship("Chapter", back_populates="pages")