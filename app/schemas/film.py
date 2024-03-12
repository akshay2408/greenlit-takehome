from typing import List

from pydantic import BaseModel


class FilmBase(BaseModel):
    title: str
    description: str
    budget: int
    release_year: int
    company_id: int
    genres: List[str]


class FilmCreate(FilmBase):
    pass


class FilmRead(FilmBase):
    id: int
    company_id: int


class FilmUpdate(FilmBase):
    pass
