from django.db import models
from datetime import date

# Create your models here.
class Threat(models.Model):
    date = models. CharField(max_length=100)
    filename = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    submit_type = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
