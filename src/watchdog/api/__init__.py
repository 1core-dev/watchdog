from fastapi import APIRouter
from .operations import router as operation_router
from .auth import router as auth_router
from .reports import router as reports_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(operation_router)
router.include_router(reports_router)
