from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database import get_db
from dtos import user as dtos
from services import users as services

db = get_db()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

@router.get("/{id}", response_model=dtos.UserRead, tags=["user"])
def get_user(id, db: Session = Depends(get_db)):
    user = services.get_user_by_id(id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("", response_model=list[dtos.UserRead], tags=["user"])
def get_users(db: Session = Depends(get_db)):
    users = services.get_users(db)
    return users