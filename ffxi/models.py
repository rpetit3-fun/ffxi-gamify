from datetime import date
from django.db import models
from django.contrib.auth.models import User

class DailyTasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today().strftime("%Y-%m-%d"))
    steps = models.PositiveIntegerField(default=0)
    pushups = models.PositiveSmallIntegerField(default=0)
    situps = models.PositiveSmallIntegerField(default=0)
    squats = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'date')