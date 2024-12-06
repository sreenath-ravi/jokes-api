from fastapi import FastAPI
from app_router import router
from db import init_db

init_db()


app = FastAPI()

app.include_router(router)
