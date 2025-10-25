from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.Manga import Manga
from schema.manga import MangaCreate, MangaUpdate, MangaRead
from typing import List

router = APIRouter(prefix="/manga", tags=["Manga"])
Error = "Manga not found"

@router.get("/", response_model=List[MangaRead])
def get_all_manga(db: Session = Depends(get_db)):
    return db.query(Manga).all()

@router.get("/{manga_id}", response_model=MangaRead)
def get_manga(manga_id: int, db: Session = Depends(get_db)):
    manga = db.query(Manga).filter(Manga.id == manga_id).first()
    if not manga:
        raise HTTPException(status_code=404, detail=Error)
    return manga

@router.post("/", response_model=MangaRead)
def create_manga(manga: MangaCreate, db: Session = Depends(get_db)):
    db_manga = Manga(**manga.dict())
    db.add(db_manga)
    db.commit()
    db.refresh(db_manga)
    return db_manga

@router.put("/{manga_id}", response_model=MangaRead)
def update_manga(manga_id: int, manga: MangaUpdate, db: Session = Depends(get_db)):
    db_manga = db.query(Manga).filter(Manga.id == manga_id).first()
    if not db_manga:
        raise HTTPException(status_code=404, detail=Error)
    for key, value in manga.dict(exclude_unset=True).items():
        setattr(db_manga, key, value)
    db.commit()
    db.refresh(db_manga)
    return db_manga

@router.delete("/{manga_id}")
def delete_manga(manga_id: int, db: Session = Depends(get_db)):
    manga = db.query(Manga).filter(Manga.id == manga_id).first()
    if not manga:
        raise HTTPException(status_code=404, detail=Error)
    db.delete(manga)
    db.commit()
    return {"detail": "Manga deleted"}
