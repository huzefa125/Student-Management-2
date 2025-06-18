from django.db import models
from students.models import Student

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    exam_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.score}"
