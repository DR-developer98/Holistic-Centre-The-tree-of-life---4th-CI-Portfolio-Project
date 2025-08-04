from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EnquiryForm

# Create your views here


def contact_tol(request):
    """
    Handles the display and submission of the contact 
    form on the 'Get in Touch' page.

    **Functionality**
    - On GET request: Renders the contact form.
    - On POST request: Validates and processes the submitted form.
      If valid, saves the enquiry and displays a success message,
      then redirects to the contact page.

    **Models Used**
    - :model:`home.Employee`

    **Context**
    - `enquiry_form`: An instance of `EnquiryForm`,
    either blank (GET) or filled with POST data.

    **Template**
    - Renders the form using: :template:`get_in_touch/contact.html`

    **Messages**
    - Displays a success notification to the user upon 
    successful form submission:
      "Thank you for reaching out to us! We will make sure to get back to you
      within 2 working days."
    """
    enquiry_form = EnquiryForm()

    if request.method == "POST":
        enquiry_form = EnquiryForm(data=request.POST)
        if enquiry_form.is_valid():
            enquiry_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for reaching out to us! We will make sure \
                    to get back to you within 2 working days.'
            )
            # ↓↓↓ CREDIT: Microsoft Copilot ↓↓↓
            return redirect('contact')

    else:
        enquiry_form = EnquiryForm()
    # ↑↑↑ CREDIT: Microsoft Copilot ↑↑↑
    return render(
        request,
        "get_in_touch/contact.html",
        {"enquiry_form": enquiry_form}
    )
