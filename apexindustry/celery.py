
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# from apex.decoraters import *

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apexindustry.settings')

app = Celery('apexindustry')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    # 'every-15-seconds' : {
    #     'task': 'apex.task.timmer',
    #     'schedule': 15,
    # },
    'active_time': {
        'task': 'apex.task.Active_time',
        'schedule':15,
    },
    # 'inactive_time':{
    #     'task': 'apex.task.Inactive_time',
    #     'schedule':15,
    # },
    # 'day_mail': {
#     #     'task': 'apex.task.daily_mail',
#     #     'schedule': 15,
#     # },
    # 'weekly_reports': {
    #     'task': 'apex.task.weekly_reports',
    #     'schedule': 30,
        # 'schedule': crontab(hour=8, minute=0),
    # },
    # 'DB_backup_drive': {
        # 'task': 'apex.task.drive_backup',
        # 'schedule': 30,
        # 'schedule': crontab(hour=8, minute=0),
    # },
    
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
