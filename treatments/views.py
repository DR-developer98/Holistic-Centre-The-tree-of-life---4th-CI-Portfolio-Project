from django.shortcuts import render
from .models import Treatment

# Create your views here


def treatments_list(request):
    """
    Renders the most recent list of treatments.
    Displays an individual instance of the
    :model:`treatments.Treatment`
    **Context**
    ``treatment``
        The most recent instances of :model:`treatments.Treatment`
    **Template**
    :template:`treatments/treatments.html`
    """
    treatments = Treatment.objects.all()

    return render(
        request,
        "treatments/treatments.html",
        {"treatments": treatments},
    )
