from re import T
from django.db import models

# Create your models here.
class bus_detail(models.Model):
    root_no = models.IntegerField(max_length=5,primary_key=True)
    driver = models.CharField(max_length=50)
    total_students = models.CharField(max_length=3)
    code = models.CharField(max_length=50)
    destination = models.CharField(max_length=100)
    stops = models.CharField(max_length=100)
    location = models.CharField(max_length=200)


