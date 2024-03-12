from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.user import CRUDManager
from app.db import get_db
from app.schemas.film import FilmCreate, FilmRead, FilmUpdate

router = APIRouter()


@router.post("/", response_model=FilmRead)
def create_film(
    film_data: FilmCreate, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Create a new film.
    """
    return crud_manager.crud_film.create(db, film_data.dict())


# Read film details by film_id
@router.get("/{film_id}", response_model=FilmRead)
def read_film(
    film_id: int, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Read film details by film_id.
    """
    film = crud_manager.crud_film.get(db, film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    return film

                                                                                
# Update film details by film_id
@router.put("/{film_id}", response_model=FilmRead)
def update_film(
    film_id: int, 
    updated_film_data: FilmUpdate, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Update film details by film_id.
    """
    film = crud_manager.crud_film.get(db, film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    film = crud_manager.crud_film.update(
        db, film, updated_film_data.dict(exclude_unset=True)
    )
    return film


# Delete film by film_id
@router.delete("/{film_id}", response_model=FilmRead)
def delete_film(
    film_id: int,
    db: Session = Depends(get_db),
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Delete film by film_id.
    """
    film = crud_manager.crud_film.get(db, film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")

    deleted_film = crud_manager.crud_film.delete(db, film_id)

    if deleted_film:
        return deleted_film
    else:
        raise HTTPException(status_code=404, detail="Film not found")

