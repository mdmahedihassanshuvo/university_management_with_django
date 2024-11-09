from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BUBT.settings')

app = Celery('BUBT')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.result_backend = 'redis://localhost:6379/0'

app.conf.result_expires = 3600
