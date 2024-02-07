from fastapi import FastAPI

from routers import router
from database import engine, Base

Base.metadata.create_all(bind=engine)

description = """
Backend service for my menu-online
"""

app = FastAPI(
    title="PRET Service Backend",
    version="0.1",
    description=description,
    redoc_url=None)

app.include_router(router)
