from django.db import models
from students.models import Student

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    due_date = models.DateField()
    payment_status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Fee for {self.student.name} - {self.amount_due}"
