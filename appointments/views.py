from django.shortcuts import render
# ↓↓↓ CREDIT: Microsoft Copilot ↓↓↓
from django.contrib.auth.decorators import login_required
# ↑↑↑ CREDIT: Microsoft Copilot ↑↑↑
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages


@login_required
def make_appointment(request):
    """
    Renders the appointment booking form in the
    'Make an appointment' page
    """
    appointment_form = AppointmentForm()

    if request.method == "POST":
        appointment_form = AppointmentForm(data=request.POST)
        if appointment_form.is_valid():
            # ↓↓↓ .cleaned_data method CREDIT: Stackoverflow ↓↓↓
            treatment = appointment_form.cleaned_data['treatment']
            appointment_date = \
                appointment_form.cleaned_data['appointment_date']
            time = appointment_form.cleaned_data['time']
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
                messages.error(request,
                               "This time slot has already been taken."
                               "Please select another one.")
            else:
                # ↓↓↓ CREDIT:
                # I think therefore I blog, Code Institute Project ↓↓↓
                appointment = appointment_form.save(commit=False)
                appointment.customer = request.user
                appointment.employee = employee
                appointment.save()
                # ↑↑↑ CREDIT:
                # I think therefore I blog, Code Institute Project ↑↑↑
                messages.success(request, "Your appointment has been booked!")
    appointment_form = AppointmentForm()

    return render(
        request,
        'appointments/make_appointment.html',
        {'appointment_form': appointment_form}
        )


@login_required
def user_appointments(request):
    """
    Display all appointments made by the currently logged-in user
    """
    appointments = Appointment.objects.filter(customer=request.user)\
        .order_by('appointment_date', 'time')

    return render(
        request,
        'appointments/my_appointments.html',
        {'appointments': appointments}
    )
