from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.models import (Company, Film, User, UserCompanyRoleAssociation,
                             UserFilmRoleAssociation)
from app.db import get_db

from .base import CRUDBase


# Define a single CRUD class for all models
class CRUDManager:
    def __init__(self, db: Session):
        self.crud_user = CRUDBase(User)
        self.crud_film = CRUDBase(Film)
        self.crud_company = CRUDBase(Company)
        self.crud_user_film = CRUDBase(UserFilmRoleAssociation)
        self.crud_user_company_association = CRUDBase(
                UserCompanyRoleAssociation)

    # Instantiate CRUDManager with dependency injection
    def get_crud_manager(db: Session = Depends(get_db)):
        return CRUDManager(db)
