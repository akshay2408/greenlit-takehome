
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.user import CRUDManager
from app.db import get_db
from app.schemas.company import CompanyCreate, CompanyRead, CompanyUpdate

router = APIRouter()

# Create a new company
@router.post("/", response_model=CompanyRead)
def create_company(
    company_data: CompanyCreate, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Create a new company.
    """
    return crud_manager.crud_company.create(db, company_data.dict())

# Read company details by company_id
@router.get("/{company_id}", response_model=CompanyRead)
def read_company(
    company_id: int, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Read company details by company_id.
    """
    company = crud_manager.crud_company.get(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

# Update company details by company_id
@router.put("/{company_id}", response_model=CompanyRead)
def update_company(
    company_id: int, 
    updated_company_data: CompanyUpdate, 
    db: Session = Depends(get_db), 
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Update company details by company_id.
    """
    company = crud_manager.crud_company.get(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    company = crud_manager.crud_company.update(
        db, company, updated_company_data.dict(exclude_unset=True)
    )
    return company


# Delete company by company_id
@router.delete("/{company_id}", response_model=CompanyRead)
def delete_company(
    company_id: int,
    db: Session = Depends(get_db),
    crud_manager: CRUDManager = Depends(CRUDManager.get_crud_manager)
):
    """
    Delete company by company_id.
    """
    company = crud_manager.crud_company.get(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="company not found")

    deleted_company = crud_manager.crud_company.delete(db, company_id)

    if deleted_company:
        return deleted_company
    else:
        raise HTTPException(status_code=404, detail="company not found")
