from .models import Appointment
from django import forms

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('treatment', 'appointment_date', 'time')