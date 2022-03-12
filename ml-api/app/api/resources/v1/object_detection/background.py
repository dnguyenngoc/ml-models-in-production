
import datetime
import json
from fastapi import UploadFile
from api.entities.object_detection import MlResult
from settings import config
from helpers import time as time_helper
from helpers.storage import upload_file_bytes, create_path
from mq_main import redis, celery_execute


def image_upload_background(file: UploadFile, 
                           task_id: str, 
                           time: datetime,
                           data: MlResult):
    file_name = task_id + config.ML_IMAGE_TYPE
    dir_path = config.ML_STORAGE_UPLOAD_PATH + time_helper.str_yyyy_mm_dd(time)    
    create_path(dir_path)
    file_path = dir_path + "/" +  file_name
    file_bytes = file.file.read()
    try:
        upload_file_bytes(file_bytes, file_path)
        # data.status['upload_id'] = task_id
        data.time['end_upload'] = str(time_helper.now_utc().timestamp())
        data.status['upload_status'] = "SUCCESS"
        data.upload_result = {"path": file_path, "file_type": config.ML_IMAGE_TYPE} 
        data_dump = json.dumps(data.__dict__)
        redis.set(task_id, data_dump)
        # print(config.ML_QUERY_NAME, config.ML_OBJECT_DETECTION_TASK)
        celery_execute.send_task(
            name="{}.{}".format(config.ML_QUERY_NAME, config.ML_OBJECT_DETECTION_TASK),
            kwargs={
                'task_id': task_id,
                'data': data_dump,
            },
            queue= config.ML_QUERY_NAME
        )
    except Exception as e:
        data.status['upload_status'] = "FAILED"
        data.status['general_status'] = "FAILED"
        data.error = str(e)
        redis.set(task_id, json.dumps(data.__dict__))