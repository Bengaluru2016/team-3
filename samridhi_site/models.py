from django.db import models
from django.utils import timezone

class Baseline(models.Model):
    """ Survey Data"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='SOME STRING')
    fname = models.CharField(max_length=200, default='SOME STRING')
    native_lang = models.CharField(max_length=200, default='SOME STRING')
    siblings = models.IntegerField(default=0)
    photo = models.BooleanField(default=False)
    age = models.IntegerField(default=False)
    date = models.DateTimeField(
                        default=timezone.now)


class Enrollment(models.Model):
    """ Enrolled data"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='SOME STRING')
    fname = models.CharField(max_length=200, default='SOME STRING')
    native_lang = models.CharField(max_length=200, default='SOME STRING')
    survey_taken = models.BooleanField(default=False)
    siblings = models.IntegerField(default=0)
    photo = models.BooleanField(default=False)
    age = models.IntegerField(default=False)
    date = models.DateTimeField(default=timezone.now)

# Create your models here.
