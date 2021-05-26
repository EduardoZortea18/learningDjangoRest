import datetime

from django.db import models


class TaskModel(models.Model):
  id: models.IntegerField(max_length=500)
  title = models.CharField(max_length=50)
  date = models.DateField(default= datetime.date)
  reminder = models.BooleanField(default=False)

  def __str__(self):
    return self.title()
