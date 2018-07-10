from flask import Flask
from celery import Celery

flask_app = Flask(__name__)

from . import tasks

@flask_app.route('/')
def index():
    tasks.add_together.delay(a=1, b=2)
    return 'ok'

if __name__ == '__main__':
    flask_app.run(port=8000, host='0.0.0.0')
