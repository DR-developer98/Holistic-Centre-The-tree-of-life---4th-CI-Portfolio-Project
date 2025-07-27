from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment
from treatments.models import Treatment
from .forms import AppointmentForm
from django.contrib import messages

# Create your views here.
def book_appointment(request):
    """ 
    Renders the appointment booking form in the 
    'Make an appointment' page 
    """
    appointment_form = AppointmentForm()

    @login_required
    if request.method == "POST":
        appointment_form = AppointmentForm(data=request.POST)
        if enquiry_form.is_valid():
            # ↓↓↓ .cleaned_data method CREDIT: Stackoverflow ↓↓↓
            treatment = form.cleaned_data['treatment']
            appointment_date = form.cleaned_data['appointment_date']
            time = form.cleaned_data['time']
            # ↑↑↑ .cleaned_data method CREDIT: Stackoverflow ↑↑↑
            employee = treatment.practitioner
            # ↓↓↓ CREDIT: Microsoft Copilot ↓↓↓
            conflict = Appointment.objects.filter(
                employee=employee,
                appointment_date=appointment_date,
                time=time
            ).exists()
            # ↑↑↑ CREDIT: Microsoft Copilot ↑↑↑

            if conflict:
                messages.error(request, "This time slot has already been taken. Please select another one.")
            else:
                # ↓↓↓ CREDIT: I think therefore I blog, Code Institute Project ↓↓↓
                appointment = form.save(commit=False)
                appointment.customer = request.user
                appointment.employee = employee
                appointment.save()
                # ↑↑↑ CREDIT: I think therefore I blog, Code Institute Project ↑↑↑
                messages.success(request, "Your appointment has been booked!")
                return redirect('appointment_confirmation')
    else:
        appointment_form = AppointmentForm()

    return render (request, 
            'book_appointment.html', 
            {'appointment_form': appointment_form}
            )
        