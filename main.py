from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from routers import router
from database import engine, Base

from database import get_db
db = get_db()
from schemas import user as schemas
from sqlalchemy.orm import Session
from services import users as user_db_services

Base.metadata.create_all(bind=engine)

description = """
Backend service for my menu-online
"""

app = FastAPI(
    title="Menu app hell yeah",
    version="0.1",
    description=description,
    redoc_url=None)

app.include_router(router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get('/test')
def test():
    return {"message": oauth2_scheme}
