from pydantic import BaseModel
from typing import List
from .film import FilmRead


class CompanyBase(BaseModel):
    name: str
    phone_number: str


class CompanyCreate(CompanyBase):
    contact_email_address: str


class CompanyRead(CompanyBase):
    id: int
    contact_email_address: str
    films: List[FilmRead]


class CompanyUpdate(CompanyBase):
    pass
