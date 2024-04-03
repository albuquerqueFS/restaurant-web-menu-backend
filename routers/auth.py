from datetime import timedelta
from typing_extensions import Annotated
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from database import get_db
from dtos import user as userSchemas, auth as authSchemas
from models import user as models
from services import auth as services

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(body: userSchemas.CreateUserRequest, db: Session = Depends(get_db)):
    new_user = models.User(
        email=body.email,
        username=body.username,
        first_name=body.first_name,
        last_name=body.last_name,
        role=body.role,
        hashed_password=bcrypt_context.hash(body.password),
        is_active=True
    )
    services.create_user(new_user, db)
    return { "message": "Usuário criado com sucesso" }


@router.post("/token", status_code=status.HTTP_200_OK, response_model=authSchemas.Token)
async def login_for_access_token(form: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = services.authenticate_user(form.username, form.password, db, bcrypt_context)

    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário ou senha incorretos")

    token = services.create_access_token(form.username, user.id, timedelta(minutes=20))

    return { 'access_token': token, 'token_type': 'bearer'}