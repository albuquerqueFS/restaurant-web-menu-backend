from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from schemas import restaurant as schemas
from models import restaurant as models
from services import restaurant as services

db = get_db()

router = APIRouter()

@router.get("/{id}", response_model=schemas.RestaurantRead, tags=["restaurant"])
def get_restaurants(id, db: Session = Depends(get_db)):
    restaurants = services.get_restaurant(id, db)
    return restaurants

@router.get("/", response_model=List[schemas.RestaurantRead], tags=["restaurant"])
def get_restaurants(db: Session = Depends(get_db)):
    restaurants = services.get_restaurants(db)
    return restaurants

@router.post("/", response_model=schemas.RestaurantCreate, tags=["restaurant"])
def create_restaurants(request: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    restaurant = services.create_restaurant(db, models.Restaurant(**request.dict()))
    return restaurant

@router.patch("/{id}", response_model=schemas.RestaurantRead, tags=["restaurant"])
def update_restaurants(id, request: schemas.RestaurantPatch, db: Session = Depends(get_db)):
    restaurant = services.update_restaurant(id, db, request)
    return restaurant