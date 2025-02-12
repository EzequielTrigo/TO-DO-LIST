from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Todo_task(models.Model):
    task_name = models.CharField(max_length=200)
    task_comments = models.CharField(max_length=20000)
    task_start_date = models.DateTimeField("start date")
    task_finished = models.BooleanField(default=False)
    task_finished_date = models.DateTimeField("finish date", null=True, blank=True)
    task_expected_finish_date = models.DateTimeField("expected finish date")

    def __str__(self):
        return self.task_name
    
    def task_not_finished_in_time(self):
        return self.task_espected_finish_Date > timezone.now()