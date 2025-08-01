from django import forms
from .models import Appointment

# Create your forms here


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('treatment', 'appointment_date', 'time')
        # ↓↓↓ CREDIT: Microsoft Copilot ↓↓↓
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
        # ↑↑↑ CREDIT: Microsoft Copilot ↑↑↑
