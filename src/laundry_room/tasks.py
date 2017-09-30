# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def get_data():
    print('Hello Celery Beat')
    return True
