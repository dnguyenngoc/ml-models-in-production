from fastapi import APIRouter
from fastapi.responses import StreamingResponse


router = APIRouter()

@router.get('/')
async def show_image(
    path_image: str,
):
    def iterfile():
        with open(path_image.replace("\\", "/"), mode="rb") as file_like:  
            yield from file_like  
    return StreamingResponse(iterfile(), media_type="image/jpeg")