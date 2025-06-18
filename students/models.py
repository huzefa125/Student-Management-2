from django.db import models
from classes.models import Class

# Create your models here.

# class Class(models.Model):
#     name = models.CharField(max_length=100)
#     # You can add a teacher ForeignKey later
#     def __str__(self):
#         return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(verbose_name='Date of Birth')
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
