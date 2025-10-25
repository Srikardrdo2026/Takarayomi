from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Favorite
from schema.favorite import FavoriteCreate, FavoriteResponse

router = APIRouter(prefix="/favorites", tags=["Favorites"])
Error = "Favorite not found"

@router.get("/", response_model=List[FavoriteResponse])
def get_favorites(db: Session = Depends(get_db)):
    return db.query(Favorite).all()

@router.post("/", response_model=FavoriteResponse)
def create_favorite(favorite: FavoriteCreate, db: Session = Depends(get_db)):
    new_fav = Favorite(**favorite.dict())
    db.add(new_fav)
    db.commit()
    db.refresh(new_fav)
    return new_fav

@router.get("/{favorite_id}", response_model=FavoriteResponse)
def get_favorite(favorite_id: int, db: Session = Depends(get_db)):
    fav = db.query(Favorite).filter(Favorite.id == favorite_id).first()
    if not fav:
        raise HTTPException(status_code=404, detail=Error)
    return fav

@router.delete("/{favorite_id}")
def delete_favorite(favorite_id: int, db: Session = Depends(get_db)):
    fav = db.query(Favorite).filter(Favorite.id == favorite_id).first()
    if not fav:
        raise HTTPException(status_code=404, detail=Error)
    db.delete(fav)
    db.commit()
    return {"detail": "Favorite deleted"}