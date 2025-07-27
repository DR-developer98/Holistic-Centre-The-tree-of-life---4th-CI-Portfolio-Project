from django.shortcuts import render
from .models import Enquiry
from .forms import EnquiryForm
from django.contrib import messages

# Create your views here.
def contact_tol(request):
    """
    Renders the contact form in the get in touch page
    """
    enquiry_form = EnquiryForm()

    if request.method == "POST":
        enquiry_form = EnquiryForm(data=request.POST)
        if enquiry_form.is_valid():
            enquiry_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for reaching out to us! We will make sure to get back to you within 2 working days.'
            )

    enquiry_form = EnquiryForm()

    return render(
        request,
        "get_in_touch/contact.html",
        {"enquiry_form": enquiry_form}
    )