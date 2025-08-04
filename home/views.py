from django.views import generic
from .models import Employee

# Create your views here


class EmployeeList(generic.ListView):
    """
    Renders the employees list in the home page
    Displays all the instances of the
    :model:`home.Employee`
    **Context**
    ``employee``
        The most recent instances of :model:`home.Employee`
    **Template**
    :template:`home/index.html`
    """
    queryset = Employee.objects.all()
    template_name = "home/index.html"
