"""
[summary] API for Paragraph, field detection of Ancestry Document project.
[information]
    @author: Duy Nguyen
    @email: duynguyenngoc@hotmail.com
    @create: 2022-1-1
"""

import logging
from logging.handlers import TimedRotatingFileHandler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request


from settings import config
from databases.connect import Session
from api.r_v1 import router_v1
from mq_main import redis



# ++++++++++++++++++++++++++++++++++++++++++++ DEFINE APP +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/openapi.json", docs_url="/api/docs", redoc_url="/api/redoc")


# ++++++++++++++++++++++++++++++++++++++++++++ HANDLE LOG FILE +++++++++++++++++++++++++++++++++++++++++++++++++++++++
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = TimedRotatingFileHandler('/logs/{}-{}-{}_{}h-00p-00.log'.format(
    config.u.year, config.u.month, config.u.day , config.u.hour), when="midnight", interval=1, encoding='utf8')
handler.suffix = "%Y-%m-%d"
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)


# ++++++++++++++++++++++++++++++++++++++++++++ ROUTER CONFIG ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
app.include_router(router_v1, prefix="/api/v1")


# ++++++++++++++++++++++++++++++++++++++++++++ CORS MIDDLEWARE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
origins = [
    "http://{host}:{port}".format(host=config.HOST, port=config.PORT),
    "http://{host}:{port}".format(host=config.HOST, port=config.FE_PORT),
    "http://{host}".format(host=config.NGINX_HOST),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ++++++++++++++++++++++++++++++++++++++++++++++ DB CONFIG ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response