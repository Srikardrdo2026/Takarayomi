from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Page
from schema.page import PageCreate, PageRead

router = APIRouter(prefix="/pages", tags=["Pages"])
Error = "Page not found"

@router.get("/chapter/{chapter_id}", response_model=List[PageRead])
def get_pages(chapter_id: int, db: Session = Depends(get_db)):
    return db.query(Page).filter(Page.chapter_id == chapter_id).all()

@router.get("/{page_id}", response_model=PageRead)
def get_page(page_id: int, db: Session = Depends(get_db)):
    page = db.query(Page).filter(Page.id == page_id).first()
    if not page:
        raise HTTPException(status_code=404, detail=Error)
    return page

@router.post("/chapter/{chapter_id}", response_model=PageRead)
def create_page(chapter_id: int, page: PageCreate, db: Session = Depends(get_db)):
    new_page = Page(**page.dict(), chapter_id=chapter_id)
    db.add(new_page)
    db.commit()
    db.refresh(new_page)
    return new_page

@router.put("/{page_id}", response_model=PageRead)
def update_page(page_id: int, page: PageCreate, db: Session = Depends(get_db)):
    existing = db.query(Page).filter(Page.id == page_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail=Error)
    for key, value in page.dict(exclude_unset=True).items():
        setattr(existing, key, value)
    db.commit()
    db.refresh(existing)
    return existing

@router.delete("/{page_id}")
def delete_page(page_id: int, db: Session = Depends(get_db)):
    page = db.query(Page).filter(Page.id == page_id).first()
    if not page:
        raise HTTPException(status_code=404, detail=Error)
    db.delete(page)
    db.commit()
    return {"detail": "Page deleted"}