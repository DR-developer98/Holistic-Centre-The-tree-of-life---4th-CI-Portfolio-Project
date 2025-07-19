from django.shortcuts import render
from django.views import generic
from .models import Employee

# Create your views here.
class EmployeeList(generic.ListView):
    queryset = Employee.objects.all()
    template_name = "landing_page.html"