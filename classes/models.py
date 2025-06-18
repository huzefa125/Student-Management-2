from django.db import models
from teachers.models import Teacher

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=100)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='classes')

    def __str__(self):
        return self.name
