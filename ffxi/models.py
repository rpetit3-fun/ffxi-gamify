from datetime import date
from django.db import models
from django.contrib.auth.models import User

class DailyTasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today().strftime("%Y-%m-%d"))
    steps = models.PositiveIntegerField(default=0)
    
    # Cardio
    jumpjacks = models.PositiveSmallIntegerField(default=0)
    high_knees = models.PositiveSmallIntegerField(default=0)
    plank_jumps = models.PositiveSmallIntegerField(default=0)
    
    # Upper Body
    pushups = models.PositiveSmallIntegerField(default=0)

    # Lower Body
    squats = models.PositiveSmallIntegerField(default=0)

    # Abs
    climbers = models.PositiveSmallIntegerField(default=0)
    knee_pull_ins = models.PositiveSmallIntegerField(default=0)
    cross_crunches = models.PositiveSmallIntegerField(default=0)
    
    # Exp Chain Acheived
    chain = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'date')

class ExperienceHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today().strftime("%Y-%m-%d"))
    exp = models.PositiveIntegerField(default=0)
    chain = models.DecimalField(max_digits=4, decimal_places=2)
    
class ExperienceStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exp = models.PositiveIntegerField(default=0)
    chain = models.DecimalField(default=1.0, max_digits=4, decimal_places=2)
