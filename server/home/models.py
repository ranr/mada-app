from django.db import models

# Create your models here.
class Event(models.Model):
    lat = models.IntegerField()
    lon = models.IntegerField()
    timestamp = models.TimeField(auto_now=True)
