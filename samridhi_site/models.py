from django.db import models
from django.utils import timezone

class Baseline(models.Model):
    """ Survey Data"""

    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    fname = models.TextField(max_length=200)
    native_lang = models.TextField(max_length=200)
    siblings = models.IntegerField(default=0)
    photo = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)


class Enrollment(models.Model):
    """ Enrolled data"""

    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    fname = models.TextField(max_length=200)
    native_lang = models.TextField(max_length=200)
    survey_taken = models.BooleanField(default=False)
    siblings = models.IntegerField(default=0)
    photo = models.BooleanField(default=False)
    age = models.IntegerField(default=False)
    date = models.DateTimeField(default=timezone.now)

class Academics(models.Model):
     id=models.AutoField(primary_key=True)
     name=models.TextField(max_length=200)
     date=models.DateTimeField(default=timezone.now)
     maths=models.IntegerField(default=00)
     science=models.IntegerField(default=00)
     english=models.IntegerField(default=00)
     hindi=models.IntegerField(default=00)
     extracuricular_activities=models.TextField(max_length=800)


class Health(models.Model):
     id=models.AutoField(primary_key=True)
     student_id = models.IntegerField(default=0)
     name=models.TextField(max_length=200)
     date=models.DateTimeField(default=timezone.now)
     student_health=models.TextField(max_length=800)
     fathers_health=models.TextField(max_length=800)
     mothers_health=models.TextField(max_length=800)
     siblings_health=models.TextField(max_length=800)
