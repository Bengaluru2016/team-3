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
    date = models.DateTimeField(
                        default=timezone.now)
class Academics(models.Model):
     id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=200,default='some string')
     date=models.DateTimeField(default=timezone.now)
     maths=models.IntegerField(default=00)
     science=models.IntegerField(default=00)
     english=models.IntegerField(default=00)
     hindi=models.IntegerField(default=00)
     extracuricular_activities=models.TextField(max_length=800)
     
     
  class Health(models.Model):
         id=models.AutoField(primary_key=True)
         name=models.CharField(max_length=200,default='some string')
         date=models.DateTimeField(default=timezone.now)
         student_health=models.TextField(max_length=800)
         fathers_health=models.TextField(max_length=800)
         mothers_health=models.TextField(max_length=800)
         siblings_health=models.TextField(max_length=800)
# Create your models here.
