from django.views import generic
from .models import Employee

# Create your views here


class EmployeeList(generic.ListView):
    queryset = Employee.objects.all()
    template_name = "home/index.html"
