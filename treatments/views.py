from django.shortcuts import render
from .models import Treatment

# Create your views here


def treatments_list(request):
    """
    Renders the Treatments page
    """
    treatments = Treatment.objects.all()

    return render(
        request,
        "treatments/treatments.html",
        {"treatments": treatments},
    )
