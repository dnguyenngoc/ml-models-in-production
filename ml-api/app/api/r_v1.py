from fastapi import APIRouter
from api.resources.v1 import account
from api.resources.v1.object_detection import router as object_detection


router_v1 = APIRouter()

router_v1.include_router(account.router, prefix="/account",  tags=["V1-Account"])
router_v1.include_router(object_detection.router, prefix="/object_detection",  tags=["V1-Object-Detection"])


