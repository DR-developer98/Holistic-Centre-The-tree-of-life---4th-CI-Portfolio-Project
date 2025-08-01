from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_tol, name='contact'),
]
