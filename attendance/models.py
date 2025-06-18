from django.db import models
from students.models import Student

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    status = models.CharField(max_length=50)  # e.g., 'Present', 'Absent', 'Late'

    def __str__(self):
        return f"{self.student.name} on {self.date}: {self.status}"
