from . import views
from django.urls import path

urlpatterns = [
    path('', views.make_appointment, name='makeappointment'),
    path('list/', views.user_appointments, name='myappointments'),
    path('appointments/edit/<int:appointment_id>/', 
         views.edit_appointment, 
         name='edit_appointment')
]