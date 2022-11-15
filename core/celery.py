from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
#pass the project name in Celery(project_name)  
app = Celery("core")

app.config_from_object('django.conf:settings', namespace='CELERY')  
# Load task modules from all registered Django apps.  
app.autodiscover_tasks() 

#Celery Beat Settings  
app.conf.beat_schedule = {
    # Scheduler Name
    'reset_fields': {
        # Task Name (Name Specified in Decorator)
        'task': 'reset_trending_field',  
        # Execute on the first day of every month      
        'schedule': crontab(0, 0, day_of_month='1'),
    }
}
  
@app.task(bind=True)  
def debug_task(self):  
    print(f'Request: {self.request!r}')  
