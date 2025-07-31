from django.urls import path
from . import views

urlpatterns = [
    path('', views.treatments_list, name='treatments'),
]
