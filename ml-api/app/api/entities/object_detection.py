from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class MlTimeHandle(BaseModel):
    start_upload: str = None
    end_upload: str = None
    start_detection: str = None
    end_detection: str = None


class MlStatusHandle(BaseModel):
    general_status: str = "PENDING"
    upload_status: str = "PENDING"
    detection_status: str = None


class MlResult(BaseModel):
    task_id: str
    status: dict = None
    time: dict = None
    upload_result: dict = None
    detection_result: list = None
    detection_draw_url: str = None
    error: Optional[str] = None
    
    
class MlResponse(BaseModel):
    status: str = "PENDING"
    status_code: int
    time: datetime
    task_id: str
    