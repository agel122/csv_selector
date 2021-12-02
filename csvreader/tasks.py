import csv
import os
from celery import shared_task

from .readfunc import csvsumm, set_file_dir
from .models import CSVdata

@shared_task
def adding_task(x, y):
    return x + y


@shared_task
def upload_data(filename):
    file_required = set_file_dir(filename)
    file_dataresult = csvsumm(file_required, 9)
    item_to_update = CSVdata.objects.get(filename=filename)
    item_to_update.dataresult = file_dataresult
    item_to_update.status = 'done'
    item_to_update.save()

