from fastapi import APIRouter
from app.api.v1.endpoints import document, analysis

api_router = APIRouter()

api_router.include_router(document.router, prefix="/documents", tags=["documents"])
api_router.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
