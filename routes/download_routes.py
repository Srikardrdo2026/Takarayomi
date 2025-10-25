from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Download
from schema.download import DownloadCreate, DownloadRead 

router = APIRouter(prefix="/downloads", tags=["Downloads"])
Error = "Download not found"

@router.get("/", response_model=List[DownloadRead])
def get_downloads(db: Session = Depends(get_db)):
    return db.query(Download).all()

@router.get("/{download_id}", response_model=DownloadRead)
def get_download(download_id: int, db: Session = Depends(get_db)):
    dl = db.query(Download).filter(Download.id == download_id).first()
    if not dl:
        raise HTTPException(status_code=404, detail=Error)
    return dl

@router.post("/", response_model=DownloadRead)
def create_download(download: DownloadCreate, db: Session = Depends(get_db)):
    new_dl = Download(**download.dict())
    db.add(new_dl)
    db.commit()
    db.refresh(new_dl)
    return new_dl

@router.put("/{download_id}", response_model=DownloadRead)
def update_download(download_id: int, download: DownloadCreate, db: Session = Depends(get_db)):
    dl = db.query(Download).filter(Download.id == download_id).first()
    if not dl:
        raise HTTPException(status_code=404, detail=Error)
    for key, value in download.dict(exclude_unset=True).items():
        setattr(dl, key, value)
    db.commit()
    db.refresh(dl)
    return dl

@router.delete("/{download_id}")
def delete_download(download_id: int, db: Session = Depends(get_db)):
    dl = db.query(Download).filter(Download.id == download_id).first()
    if not dl:
        raise HTTPException(status_code=404, detail=Error)
    db.delete(dl)
    db.commit()
    return {"detail": "Download deleted"}
