# -----------------------------------------------------------
# API paragraph and field detection for ancestry document
# (C) 2021 Duy Nguyen, Ho Chi Minh, Viet Nam
# email duynguyenngoc@hotmail.com
# -----------------------------------------------------------

from fastapi import APIRouter, UploadFile, File, Form, BackgroundTasks, HTTPException, Depends
from starlette.status import (
    HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
)
import uuid
import json
from mq_main import redis
from securities import token as token_helper
from helpers import time as time_helper
from settings import config
from api.entities.object_detection import MlTimeHandle, MlResult, MlStatusHandle, MlResponse
from api.resources.v1.object_detection.background import image_upload_background


router = APIRouter()


@router.post("/process")
async def ml_process(
    *,
    # current_user = Depends(token_helper.get_current_user),
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks
):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="file_type not support!")
    time = time_helper.now_utc()
    task_id = str(uuid.uuid5(uuid.NAMESPACE_OID, config.ML_QUERY_NAME + "_"+ str(time)))
    time_handle = MlTimeHandle(start_upload=str(time.timestamp())).__dict__
    status_hanlde = MlStatusHandle().__dict__
    data = MlResult(task_id=task_id, time=time_handle, status=status_hanlde)
    redis.set(task_id, json.dumps(data.__dict__))
    background_tasks.add_task(image_upload_background, file, task_id, time, data)
    return MlResponse(status="PENDING", time=time, status_code=HTTP_200_OK, task_id=task_id)


@router.get("/status/{task_id}", response_model=MlResult)
def ml_status(
    *,
    task_id: str,
    # current_user = Depends(token_helper.get_current_user),
):
    data = redis.get(task_id)
    if data == None:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail='task id not found!')
    message = json.loads(data)
    return message
