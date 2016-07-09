from django.db import models
from django.utils import timezone

class Baseline(models.Model):
    """ Survey Data"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    fathersname = models.CharField(max_length=200)

# Create your models here.
