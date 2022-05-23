from django.db import models
from incharge.models import bus_detail
from student.models import students
# Create your models here.
class parent(models.Model):
    name = models.CharField(max_length=50)
    child = models.ForeignKey(students, on_delete=models.CASCADE)
    bus = models.ForeignKey(bus_detail, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=50)