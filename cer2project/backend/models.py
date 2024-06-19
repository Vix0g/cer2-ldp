from django.db import models
#from rest_framework import viewsets

# Create your models here.

class Number(models.Model):
    number = models.IntegerField()
    letter = models.CharField()
