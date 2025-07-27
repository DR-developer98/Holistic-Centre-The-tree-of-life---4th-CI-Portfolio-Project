from django.db import models
from django.contrib.auth.models import User
from treatments.models import Treatment
from home.models import Employee

# Create your models here.
class Appointment(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    time = models.TimeField()

    # ↓↓↓ CREDIT: Microsoft Copilot ↓↓↓
    class Meta:
        unique_together = ('employee', 'appointment_date', 'time')
    # ↑↑↑ CREDIT: Microsoft Copilot ↑↑↑

    def __str__(self):
        return f"{self.customer.username} - {self.appointment_date} {self.time}"