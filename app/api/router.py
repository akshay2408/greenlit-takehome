from fastapi import APIRouter

from .routes.company import router as company_router
from .routes.films import router as film_router
from .routes.user import router as user_router

api_router = APIRouter()

api_router.include_router(user_router, prefix="/user", tags=["user"])
api_router.include_router(film_router, prefix="/film", tags=["film"])
api_router.include_router(company_router, prefix="/company", tags=["company"])


