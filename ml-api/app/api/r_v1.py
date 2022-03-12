from fastapi import APIRouter
from api.resources.v1 import account


router_v1 = APIRouter()

router_v1.include_router(account.router, prefix="/account",  tags=["V1-Account"])

