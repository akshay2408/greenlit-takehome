from typing import Union

from fastapi import FastAPI

from .api.router import api_router
from .core import models
from .db import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(api_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}