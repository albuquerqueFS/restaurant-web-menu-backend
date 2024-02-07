from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from schemas import menu as schemas
from models import menu as models
from services import menu as services

db = get_db()

router = APIRouter()

@router.get("/{id}", response_model=schemas.RestaurantRead, tags=["menu"])
def get_menus(id, db: Session = Depends(get_db)):
    menus = services.get_menu(id, db)
    return menus

@router.get("/", response_model=List[schemas.RestaurantRead], tags=["menu"])
def get_menus(db: Session = Depends(get_db)):
    menus = services.get_menus(db)
    return menus

@router.post("/", response_model=schemas.RestaurantCreate, tags=["menu"])
def create_menus(request: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    menu = services.create_menu(db, models.Menu(**request.dict()))
    return menu

@router.patch("/{id}", response_model=schemas.RestaurantRead, tags=["menu"])
def update_menus(id, request: schemas.RestaurantPatch, db: Session = Depends(get_db)):
    menu = services.update_menu(id, db, request)
    return menu