"""Module with Celery configurations to Audio Length worker."""
from kombu import Queue
import configparser


cfg = configparser.ConfigParser()
cfg.read('./environment.ini')

#=========================================================================
#                          CELERY INFORMATION 
#=========================================================================
CELERY = cfg['celery']

# Set worker to ack only when return or failing (unhandled expection)
task_acks_late = True

# Worker only gets one task at a time
worker_prefetch_multiplier = 1

QUERY_NAME = CELERY["query"]

# Create queue for worker
task_queues = [Queue(name=QUERY_NAME)]

# Set Redis key TTL (Time to live)
result_expires = 60 * 60 * 48  # 48 hours in seconds


# #=========================================================================
# #                          ML INFORMATION 
# #=========================================================================
ML_OBJECT_DETECTION_TASK_NAME = CELERY['object_detection_task']
ML_STORAGE_PATH = CELERY['storage_path']
ML_STORAGE_UPLOAD_PATH = CELERY['storage_upload_path']
ML_STORAGE_OBJECT_DETECTION_PATH = CELERY['storage_object_detection_path']
ML_IMAGE_TYPE = CELERY['image_type']
