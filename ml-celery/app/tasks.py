"""[summary]
 @author Duy Nguyen Ngoc - duynguyenngoc@hotmail.com
"""

import json
import logging
import cv2
from celery import Celery, Task
from init_broker import is_broker_running
from init_redis import is_backend_running

from settings import config
from mq_main import redis


from worker.ml.model import CompletedModel
from worker.ml.helpers import image_utils as ml_image_helper
from helpers import time as time_helper
from settings import (celery_config, config, ml_config)
from helpers.storage import create_path


if not is_backend_running(): exit()
if not is_broker_running(): exit()


app = Celery(celery_config.QUERY_NAME, broker=config.BROKER, backend=config.REDIS_BACKEND)
app.config_from_object('settings.celery_config')


class PredictTask(Task):
    """
    Abstraction of Celery's Task class to support loading ML model.
    """
    abstract = True

    def __init__(self):
        super().__init__()
        self.model = None

    def __call__(self, *args, **kwargs):
        """
        Load model on first call (i.e. first task processed)
        Avoids the need to load model on each task request
        """
        if not self.model:
            logging.info('Loading Model...')
            self.model = CompletedModel()
            logging.info('Model loaded')
        return self.run(*args, **kwargs)
    
@app.task(bind=True, 
          base=PredictTask,
          name="{query}.{task_name}".format(
              query=celery_config.QUERY_NAME, 
              task_name=celery_config.ML_OBJECT_DETECTION_TASK_NAME))
def object_detection_task(self, task_id: str, data: bytes):
    """_summary_: object_detection by efi d2 model

    Args:
        task_id (str): _description_
        data (bytes): _description_

    Returns:
        _type_: _description_
    """
    data = json.loads(data) # load session data
    time = time_helper.now_utc()
    data['time']['start_detection'] = str(time_helper.now_utc().timestamp())
    string_time = time_helper.str_yyyy_mm_dd(time)
    try:
        image = ml_image_helper.read_image_from_path_to_numpy(data['upload_result']['path'])
        image_draw = image.copy()
        height, width = image.shape[0:2]
        detections, category_index = self.model.detect(image)
        detection_boxes = detections['detection_boxes']
        detection_scores = detections['detection_scores']
        detection_classes = detections['detection_classes']
        det_new = []
        class_name_color = (0,255,0)
        box_color = (0,255,0)
        for j in range(len(detection_boxes)):
            box = detection_boxes[j]
            ymin, xmin, ymax, xmax = int(box[0]*height), int(box[1]*width), int(box[2]*height), int(box[3]*width)
            obj = {}
            obj['confidence_level'] = str(detection_scores[j])
            obj['box'] = ",".join([str(xmin), str(ymin), str(xmax), str(ymax)])
            obj['class_name'] = category_index[detection_classes[j]]['name']
            det_new.append(obj)
            image_draw = cv2.rectangle(image_draw, (xmin, ymin), (xmax, ymax), box_color, 1)
            cv2.putText(image_draw, obj['class_name'], (xmin+5, ymin+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, class_name_color, 2)
        data['detection_draw_url'] = "http://{}:{}/api/v1/show-image/?path_image=".format(config.BE_HOST, config.BE_PORT) \
            + celery_config.ML_STORAGE_OBJECT_DETECTION_PATH + string_time + '/' + str(task_id) + celery_config.ML_IMAGE_TYPE
        create_path(celery_config.ML_STORAGE_OBJECT_DETECTION_PATH + string_time)
        cv2.imwrite(celery_config.ML_STORAGE_OBJECT_DETECTION_PATH + string_time + '/' + str(task_id) + celery_config.ML_IMAGE_TYPE, image_draw)
        data['time']['end_detection'] = str(time_helper.now_utc().timestamp())
        data['status']['detection_status'] = "SUCCESS"
        if len(det_new) > 0:
            data['detection_result'] = det_new
        data['status']['general_status'] = "SUCCESS"
        data_dump = json.dumps(data)
        redis.set(task_id, data_dump) 
    except Exception as e:
        data['time']['end_detection'] = str(time_helper.now_utc().timestamp())
        data['status']['detection_status'] = "FAILED"
        data['status']['general_status'] = "FAILED"
        data['error'] = str(e)
        data_dump = json.dumps(data)
        redis.set(task_id, data_dump)
        