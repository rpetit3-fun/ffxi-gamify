from django.db import models

# Create your models here.
class Titles(models.Model):
    title_id =models.PositiveSmallIntegerField(primary_key=True)
    title = models.TextField()
