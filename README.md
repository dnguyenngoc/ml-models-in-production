# Ml Models in Production
[![python](https://img.shields.io/badge/python-3.9.5-green)](https://www.python.org/doc/)
[![Celery](https://img.shields.io/badge/celery-5.2.3-green)](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
[![Rabbitmq](https://img.shields.io/badge/rabbitmq-3-orange)](https://www.rabbitmq.com/)
[![Redis](https://img.shields.io/badge/redis-6.2.6-orange)](https://redis.io/)
[![react](https://img.shields.io/badge/react-17.0.2-lightgrey)](https://reactjs.org/)
[!]

This repo gives an introduction to how to make full working example to serve your model using asynchronous Celery tasks and FastAPI. This post walks through a working example for serving a ML model using Celery and FastAPI. All code can be found in this repository. We won’t specifically discuss the ML model used for this example however it was trained using coco dataset with 90 object class like cat, dog, bird ... more detail here [Coco Dataset](https://cocodataset.org/#home). The model have been train with tensorflow [Tensorflow](https://github.com/tensorflow/models) 

## Screenshots & Gifs

**View System**
[![Architecture](public/architecture.png)


## Contents
- [Screenshots & Gifs](#screenshots--gifs)
- [Example](#example)
    - [1. Install docker, docker-compose](https://github.com/apot-group/real-time-analytic#1-install-docker-and-docker-compose)
    - [2. Pull git repo](https://github.com/apot-group/real-time-analytic#2-pull-git-repo)
    - [3. Start Server](https://github.com/apot-group/real-time-analytic#3-start-server)
- [Contact Us](#contact-us)


## Example

### 1. Install docker and docker-compose

`https://www.docker.com/`

### 2. Pull git repo
`git clone https://github.com/apot-group/real-time-analytic.git` 

### 3. Start Server
`cd real-time-analytic && docker-compose up`

| Service               | URL                              | User/Password                                 |
| :-------------------: | :------------------------------: | :-------------------------------------------: |
| Druid Unified Console | http://localhost:8888/           | None                                          |
| Druid Legacy Console  | http://localhost:8081/           | None                                          |
| Superset              | http://localhost:8088/           | docker exec -it superset bash superset-init   |
| Airflow               | http://localhost:3000/           | a-airflow/app/standalone_admin_password.txt   |

### 3. Create Dashboard sample from druid streaming
 - Airflow dags at a-airflow/app/dags/demo.py each one min sent message to kafka 'demo' topic with data of list coin ['BTC', 'ETH', 'BTT', 'DOT'] the structure of data message like below.
```
   {
        "data_id" : 454,
        "name": 'BTC',
        "timestamp": '2021-02-05T10:10:01'
    }
```

 - From druid load data from kafka ```kafka:9092```, choice ```demo``` topic and config data result table
<div>
    <img src="https://github.com/apot-group/real-time-analytic/blob/main/public/druid_connect.gif" />
</div>
<br>

 - From superset add druid like database sqlalchemy uri: ```druid://broker:8082/druid/v2/sql/```. more detail at [Superset-Database-Connect](https://superset.apache.org/docs/databases/db-connection-ui)
 - Create Chart and dashboard on superset from ```demo``` table.
 - Enjoy! :fire: :fire: :fire:

## Contact Us
- Email-1: duynnguyenngoc@hotmail.com - Duy Nguyen :heart: :heart: :heart: 