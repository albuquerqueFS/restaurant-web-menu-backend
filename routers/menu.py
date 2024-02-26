from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from schemas import menu as schemas
from models import menu as models
from services import menu as services

db = get_db()

router = APIRouter()

@router.get("/{id}", response_model=schemas.MenuRead, tags=["menu"])
def get_menus(id, db: Session = Depends(get_db)):
    menus = services.get_menu(id, db)
    return menus

@router.get("/", response_model=List[schemas.MenuRead], tags=["menu"])
def get_menus(db: Session = Depends(get_db)):
    menus = services.get_menus(db)
    return menus

@router.post("/", response_model=schemas.MenuRead, tags=["menu"])
def create_menus(restaurant_id: int, request: schemas.MenuCreate, db: Session = Depends(get_db)):
    menu = services.create_menu(db, restaurant_id, models.Menu(**request.dict(), restaurant_id=restaurant_id))
    return menu

@router.patch("/{id}", response_model=schemas.MenuRead, tags=["menu"])
def update_menus(id, request: schemas.MenuPatch, db: Session = Depends(get_db)):
    menu = services.update_menu(id, db, request)
    return menu