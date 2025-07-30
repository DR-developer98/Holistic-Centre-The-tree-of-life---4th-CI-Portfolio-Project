from . import views
from django.urls import path

urlpatterns = [
    path('', views.make_appointment, name='makeappointment'),
    path('list/', views.user_appointments, name='myappointments'),
]