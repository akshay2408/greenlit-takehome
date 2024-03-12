from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.user import CRUDManager
from app.db import get_db
from app.schemas.user import (UserCompanyAssociationCreate,
                              UserCompanyAssociationRead,
                              UserCompanyAssociationUpdate, UserCreate,
                              UserFilmAssociationBase,
                              UserFilmAssociationCreate,
                              UserFilmAssociationUpdate, UserRead, UserUpdate)

router = APIRouter()


# Create a new user
@router.post("/", response_model=UserRead)
def create_user(
    user_data: UserCreate, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Create a new user.
    """
    return crud_manager.crud_user.create(db, user_data.dict())


# Read user details by user_id
@router.get("/{user_id}", response_model=UserRead)
def get_user(
    user_id: int, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Read user details by user_id.
    """
    user = crud_manager.crud_user.get(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# # Update user details by user_id
@router.put("/{user_id}", response_model=UserRead)
def update_user(
    user_id: int, 
    updated_user_data: UserUpdate, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Update user details by user_id.
    """
    user = crud_manager.crud_user.get(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = crud_manager.crud_user.update(db, user, updated_user_data.dict(exclude_unset=True))
    return user


# Delete user by user_id
@router.delete("/{user_id}", response_model=UserRead)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Delete user by user_id.
    """
    user = crud_manager.crud_user.get(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    deleted_user = crud_manager.crud_user.delete(db, user_id)

    if deleted_user:
        return deleted_user
    else:
        raise HTTPException(status_code=404, detail="user not found")


# # Create association between user and film
@router.post("/create-users-film", response_model=UserFilmAssociationBase)
def create_users_film(
    data: UserFilmAssociationCreate, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Create association between user and film.
    """
    user = crud_manager.crud_user.get(db, data.user_id)
    film = crud_manager.crud_film.get(db, data.film_id)
    if user is None or film is None:
        raise HTTPException(status_code=404, detail="User or Film not found")
    return crud_manager.crud_user_film.create(db, data.dict())


# # Update association between user and film by user_film_id
@router.patch("/update-users-film/{user_film_id}", response_model=UserFilmAssociationBase)
def update_users_film(
    user_film_id: int, 
    update_userfilm_data: UserFilmAssociationUpdate, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Update association between user and film by user_film_id.
    """
    user = None
    film = None
    if update_userfilm_data.user_id:
        user = crud_manager.crud_user.get(db, update_userfilm_data.user_id)
    if update_userfilm_data.film_id:
        film = crud_manager.crud_film.get(db, update_userfilm_data.film_id)
    if user is None or film is None:
        raise HTTPException(status_code=404, detail="User or Film not found")
    user_films = crud_manager.crud_user_film.get(db, user_film_id)
    if not user_films:
        raise HTTPException(status_code=404, detail="User Films Association not found")
    return crud_manager.crud_user_film.update(db, user_films, update_userfilm_data.dict(exclude_unset=True))


# Read association between user and film by user_film_id
@router.get("/get-users-film-association/{user_film_id}")
def get_users_film_association(
    user_film_id: int, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Read association between user and film by user_film_id.
    """
    user_films = crud_manager.crud_user_film.get(db, user_film_id)
    if not user_films:
        raise HTTPException(status_code=404, detail="User Films Association not found")
    return user_films


# Create association between user and company
@router.post("/create-users-company-association", response_model=UserCompanyAssociationRead)
def create_users_company_association(
    data: UserCompanyAssociationCreate,
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Create association between user and company.
    """
    user_file_obj = data.dict()
    user = crud_manager.crud_user.get(db, user_file_obj['user_id'])
    company = crud_manager.crud_company.get(db, user_file_obj['company_id'])
    if user is None or company is None:
        raise HTTPException(status_code=404, detail="User or Company not found")
    return crud_manager.crud_user_company_association.create(db, data.dict())


# Update association between user and company by user_company_id
@router.patch("/update-users-company-association/{user_company_id}", 
              response_model=UserCompanyAssociationRead)
def update_users_company_association(
    user_company_id: int, 
    update_usercompany_data: UserCompanyAssociationUpdate, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Update association between user and company by user_company_id.
    """
    user_id = update_usercompany_data.user_id
    company_id = update_usercompany_data.company_id
    user = None
    company = None
    if user_id:
        user = crud_manager.crud_user.get(db, user_id)
    if company_id:
        company = crud_manager.crud_company.get(db, company_id)
    if user is None or company is None:
        raise HTTPException(status_code=404, detail="User or Company not found")
    user_company = crud_manager.crud_user_company_association.get(db, user_company_id)
    if not user_company:
        raise HTTPException(status_code=404, detail="User Company Association not found")
    return crud_manager.crud_user_company_association.update(db, user_company, update_usercompany_data.dict(exclude_unset=True))


# Read association between user and company by user_company_id
@router.get("/get-users-company-association/{user_company_id}")
def get_users_company_association(
    user_company_id: int, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Read association between user and company by user_company_id.
    """
    user_company = crud_manager.crud_user_company_association.get(db, user_company_id)
    if not user_company:
        raise HTTPException(status_code=404, detail="User Company Association not found")
    return user_company
