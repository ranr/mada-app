from django.db import models

# Create your models here.
class Event(models.Model):
    latitude    = models.FloatField()
    longitude   = models.FloatField()
    timestamp   = models.DateTimeField(auto_now=True)
    information = models.CharField(max_length=200)
    address     = models.CharField(max_length=200)

class Rescuer(models.Model):
    latitude            = models.FloatField()
    longitude           = models.FloatField()
    last_update_time    = models.DateTimeField(auto_now=True)
    rank                = models.CharField(max_length=100)
    phone_number        = models.CharField(max_length=30, unique=True)