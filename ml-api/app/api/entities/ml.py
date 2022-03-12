from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class MlTimeHandle(BaseModel):
    start_upload: str = None
    end_upload: str = None
    start_paragraph: str = None
    end_paragraph: str = None
    start_field: str = None
    end_field: str = None


class MlStatusHandle(BaseModel):
    general_status: str = "PENDING"
    upload_status: str = "PENDING"
    paragraph_status: str = None
    field_status: str = None


class MlResult(BaseModel):
    task_id: str
    status: dict = None
    time: dict = None
    upload_result: dict = None
    paragraph_result: dict = None
    field_result: dict = None
    error: Optional[str] = None
    
class MlResponse(BaseModel):
    status: str = "PENDING"
    status_code: int
    time: datetime
    task_id: str
    