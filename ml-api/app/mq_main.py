from redis import Redis
from settings import config
from celery import Celery


redis = Redis(host=config.REDIS['host'], port=config.REDIS['port'], password=config.REDIS['pass'], db= config.REDIS['db'])


celery_execute = Celery(broker=config.BROKER, backend=config.REDIS_BACKEND)
