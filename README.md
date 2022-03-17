# Ml Models in Production
[![python](https://img.shields.io/badge/python-3.9.5-green)](https://www.python.org/doc/)
[![Celery](https://img.shields.io/badge/celery-5.2.3-green)](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
[![rabbitmq](https://img.shields.io/badge/rabbitmq-3-orange)](https://www.rabbitmq.com/)
[![redis](https://img.shields.io/badge/redis-6.2.6-orange)](https://redis.io/)
[![react](https://img.shields.io/badge/react-17.0.2-lightgrey)](https://reactjs.org/)
[![fastapi](https://img.shields.io/badge/fastapi-0.75.0-blue)](https://fastapi.tiangolo.com/)
[![NPM](https://img.shields.io/badge/npm-1.0.1-green)](https://www.npmjs.com/package/package/v/1.0.1)
[![Tensorflow](https://img.shields.io/badge/tensorflow-3.7-yellowgreen)](https://analyticsindiamag.com/tensorflow-2-7-0-released-all-major-updates-features/)


This repo gives an introduction to how to make full working example to serve your model using asynchronous Celery tasks and FastAPI. This post walks through a working example for serving a ML model using Celery and FastAPI. All code can be found in this repository. We won’t specifically discuss the ML model used for this example however it was trained using coco dataset with 80 object class like cat, dog, bird ... more detail here [Coco Dataset](https://cocodataset.org/#home). The model have been train with tensorflow [Tensorflow](https://github.com/tensorflow/models) 


## Contents
- [Screenshots & Gifs](#screenshots--gifs)
- [Demo](#demo)
    - [1. Install docker, docker-compose](#1-install-docker-and-docker-compose)
    - [2. Pull git repo](#2-pull-git-repo)
    - [3. Start Server](#3-start-server)
- [Contact Us](#contact-us)


## Screenshots & Gifs

**View System**

![Architecture](public/architecture.png)


## Demo

### 1. Install docker and docker-compose

`https://www.docker.com/`

### 2. Pull git repo
`git clone https://github.com/apot-group/ml-models-in-production.git` 

### 3. Start Server
`cd ml-models-in-production && docker-compose up`

| Service               | URL                              | 
| :-------------------: | :------------------------------: | 
| API docs              | http://localhost/api/docs        |
| Demo Web              | http://localhost                 | 

go to Demo web ```http://localhost``` and test with your picture.

![Test](public/test.png)

## Contact Us
- Email-1: duynnguyenngoc@hotmail.com - Duy Nguyen :heart: :heart: :heart: 