from fastapi import FastAPI

from .database.create_table import create_table
from .routes.links import router

create_table()

app = FastAPI()

app.include_router(router)