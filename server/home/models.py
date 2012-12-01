from django.db import models

# Create your models here.
class Event(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

