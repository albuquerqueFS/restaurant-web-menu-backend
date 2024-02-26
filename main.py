import os
import uvicorn

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from routers import router
from database import engine, Base

from database import get_db
db = get_db()

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

@app.get('/health')
def test():
    return { "message": "i'm alive" }

if __name__ == '__main__':
    uvicorn.run("main:app", host=os.environ.get("HOST"), port=os.environ.get("PORT"), reload=True)
