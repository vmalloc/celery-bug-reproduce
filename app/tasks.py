import time
from celery import Celery

celery = Celery(__name__,
                broker='amqp://guest:guest@rabbitmq', backend='rpc://')

@celery.task()
def add_together(a, b):
    with open('/tmp/outputs.txt', 'a') as f:
        print(time.asctime(), file=f)
