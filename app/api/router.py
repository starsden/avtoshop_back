from fastapi import APIRouter

from app.api.routes import auth, legacy, reviews, services

api_router = APIRouter(prefix="/api")
api_router.include_router(auth.router)
api_router.include_router(services.router)
api_router.include_router(reviews.router)
api_router.include_router(legacy.router)
