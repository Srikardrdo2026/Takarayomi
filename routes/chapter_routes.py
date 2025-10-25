from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.Chapter import Chapter
from schema.chapter import ChapterCreate, ChapterRead
from typing import List

router = APIRouter(prefix="/chapters", tags=["Chapters"])
Error = "Chapter not found"

@router.get("/manga/{manga_id}", response_model=List[ChapterRead])
def get_chapters(manga_id: int, db: Session = Depends(get_db)):
    return db.query(Chapter).filter(Chapter.manga_id == manga_id).all()

@router.get("/{chapter_id}", response_model=ChapterRead)
def get_chapter(chapter_id: int, db: Session = Depends(get_db)):
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail=Error)
    return chapter

@router.post("/manga/{manga_id}", response_model=ChapterRead)
def create_chapter(manga_id: int, chapter: ChapterCreate, db: Session = Depends(get_db)):
    new_chapter = Chapter(**chapter.dict(), manga_id=manga_id)
    db.add(new_chapter)
    db.commit()
    db.refresh(new_chapter)
    return new_chapter

@router.put("/{chapter_id}", response_model=ChapterRead)
def update_chapter(chapter_id: int, chapter: ChapterCreate, db: Session = Depends(get_db)):
    existing = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail=Error)
    for key, value in chapter.dict(exclude_unset=True).items():
        setattr(existing, key, value)
    db.commit()
    db.refresh(existing)
    return existing

@router.delete("/{chapter_id}")
def delete_chapter(chapter_id: int, db: Session = Depends(get_db)):
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail=Error)
    db.delete(chapter)
    db.commit()
    return {"detail": "Chapter deleted"}
