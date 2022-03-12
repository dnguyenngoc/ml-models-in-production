from fastapi import APIRouter
from api.resources.v1 import account, show_image
from api.resources.v1.object_detection import router as object_detection


router_v1 = APIRouter()

router_v1.include_router(account.router, prefix="/account",  tags=["V1-Account"])
router_v1.include_router(object_detection.router, prefix="/object-detection",  tags=["V1-Object-Detection"])
router_v1.include_router(show_image.router, prefix="/show-image",  tags=["V1-Image"])



