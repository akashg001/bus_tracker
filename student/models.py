from pyexpat import model
from statistics import mode
from django.db import models
from incharge.models import bus_detail
# Create your models here.
class students(models.Model):
    roll_no = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=50)
    bus = models.ForeignKey(bus_detail, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    locations = models.CharField(max_length=200)