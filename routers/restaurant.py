from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List
from sqlalchemy.orm import Session

from database import get_db
from schemas import restaurant as schemas
from models import restaurant as models
from services import restaurant as services
from services.auth import get_current_user

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

router = APIRouter()

@router.get("/{id}", response_model=schemas.RestaurantRead, tags=["restaurant"])
def get_restaurants(id, db: db_dependency):
    restaurants = services.get_restaurant(id, db)
    return restaurants

@router.get("/", response_model=List[schemas.RestaurantRead], tags=["restaurant"])
def get_restaurants(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Autenticação falhou')
    restaurants = services.get_restaurants(db)
    return restaurants

@router.post("/", response_model=schemas.RestaurantCreate, tags=["restaurant"])
def create_restaurants(request: schemas.RestaurantCreate, user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Autenticação falhou')

    restaurant = services.create_restaurant(db, models.Restaurant(**request.dict(), user_id=user.get('id')))
    return restaurant

@router.patch("/{id}", response_model=schemas.RestaurantRead, tags=["restaurant"])
def update_restaurants(id, request: schemas.RestaurantPatch, db: db_dependency):
    restaurant = services.update_restaurant(id, db, request)
    return restaurant