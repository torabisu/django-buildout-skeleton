from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    #------------------------------------------------------------------------------------------------------[ Hosting ]--
    'sync-level-3': {
        'task': 'opt.hosting.tasks.sync_level3_stats',
        'schedule': crontab(hour=1, minute=30),
    },
    'hello-world': {
        'task': 'opt.hosting.tasks.hello_world',
        'schedule': timedelta(minutes=1)
    },
}
