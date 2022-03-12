from redis import Redis
from settings import config


redis = Redis(
    host=config.REDIS['host'], 
    port=config.REDIS['port'], 
    password=config.REDIS['pass'],
    db= config.REDIS['db']
)
