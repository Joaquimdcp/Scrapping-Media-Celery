import os
import logging
from celery import Celery

backend = os.getenv('CELERY_BACKEND_URL', 'amqp')
celery = Celery('tasks', backend=backend)

@celery.task
def add(x, y):
    return x + y