from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_appointment, name='makeappointment'),
    path('list/', views.user_appointments, name='myappointments'),
    path('edit/<int:appointment_id>/',
         views.edit_appointment,
         name='edit_appointment'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment,
         name='cancel_appointment'),
]
