import configparser
import datetime
import pytz 


cfg = configparser.ConfigParser()
cfg.read('./environment.ini')


#=========================================================================
#                           TIMING CONFIG
#=========================================================================
u = datetime.datetime.utcnow()
u = u.replace(tzinfo=pytz.timezone("Asia/Ho_Chi_Minh"))

#=========================================================================
#                          PROJECT INFORMATION 
#=========================================================================
PROJECT = cfg['project']
BE_HOST = PROJECT['be_host']
BE_PORT = PROJECT['be_port']

#=========================================================================
#                          REDIS INFORMATION 
#=========================================================================
REDIS = cfg['redis']
REDIS_BACKEND = "redis://:{password}@{hostname}:{port}/{db}".format(
    hostname=REDIS['host'],
    password=REDIS['pass'],
    port=REDIS['port'],
    db=REDIS['db']
)

#=========================================================================
#                          BROKER INFORMATION 
#=========================================================================
RABBITMQ = cfg['rabbitmq']
BROKER = "amqp://{user}:{pw}@{hostname}:{port}/{vhost}".format(
    user=RABBITMQ['user'],
    pw=RABBITMQ['pass'],
    hostname=RABBITMQ['host'],
    port=RABBITMQ['post'],
    vhost=RABBITMQ['vhost']
)
