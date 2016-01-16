# DigitGuesser

A web service created using HTML5/JS, Flask, Celery and Redis.

User draws a digit on a canvas and the service tries to guess it using KNN-algorithm.

## Requirements
- Redis
- Python

Python dependencies
- flask
- celery
- numpy
- sklearn

## How to run
Configure Redis address in celery_app.py.
```
Start Celery and Flask services:
$ python celery_app.py
$ python service.py
```

Navigate to http://localhost:5000
