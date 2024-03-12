from enum import Enum

from pydantic import BaseModel

from .film import FilmRead


class UserCompanyRoleEnum(Enum):
    owner = "owner"
    member = "member"


class UserRoleEnum(Enum):
    writer = "writer"
    producer = "producer"
    director = "director"


class UserBase(BaseModel):
    first_name: str
    last_name: str
    minimum_fee: int


class UserCreate(UserBase):
    email: str


class UserRead(UserBase):
    id: int
    email: str


class UserUpdate(UserBase):
    pass


class UserFilmAssociationBase(BaseModel):
    user_id: int
    film_id: int
    role: str


class UserFilmAssociationCreate(UserFilmAssociationBase):
    pass


class UserFilmAssociationUpdate(UserFilmAssociationBase):
    pass


class UserFilmAssociationRead(UserFilmAssociationBase):
    user_id: UserRead
    film_id: FilmRead
    role: UserRoleEnum


class UserCompanyAssociationBase(BaseModel):
    user_id: int
    company_id: int
    role: str


class UserCompanyAssociationCreate(UserCompanyAssociationBase):
    pass


class UserCompanyAssociationUpdate(UserCompanyAssociationBase):
    pass


class UserCompanyAssociationRead(UserCompanyAssociationBase):
    user_id: int
    company_id: int
    role: UserCompanyRoleEnum
