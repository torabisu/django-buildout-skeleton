from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'hello-world': {
        'task': 'opt.hosting.tasks.hello_world',
        'schedule': timedelta(minutes=1)
    },
}
