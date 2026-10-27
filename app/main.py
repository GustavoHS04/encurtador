from fastapi import FastAPI

from .database.create_table import create_links, create_acessos
from .routes.links import router

create_links()
create_acessos()

app = FastAPI()

app.include_router(router)