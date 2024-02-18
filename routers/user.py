from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Dict
from sqlalchemy.orm import Session

from database import get_db
from schemas import user as schemas
from services import users as services
from models import user as models

db = get_db()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

@router.get("/{id}", response_model=schemas.UserRead, tags=["user"])
def get_user(id, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = services.get_user_by_id(id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=schemas.UserCreate, tags=["user"])
def create_user(request: schemas.UserCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = services.create_user(db, models.User(**request.dict()))
    return user

@router.post('/login', response_model=Dict)
def login(
    payload:OAuth2PasswordBearer = Depends(),
    session: Session = Depends(get_db)
):
    try:
        user: models.User = services.get_user_by_id(session, payload.username)
    except:
        raise HTTPException(status_code=404, detail="User not found")

    # is_validated: bool = user.