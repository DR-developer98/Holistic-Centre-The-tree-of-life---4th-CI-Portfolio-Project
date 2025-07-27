from django.contrib import admin
from .models import Appointment

# Register your models here.
@admin.register(Appointment)
class CustomerAppointment(admin.ModelAdmin):

    list_display = ('customer', 'treatment', 'employee', 'appointment_date', 'time',)