from django.shortcuts import render, redirect, get_object_or_404
# ↓↓↓ CREDIT: Microsoft Copilot ↓↓↓
from django.contrib.auth.decorators import login_required
# ↑↑↑ CREDIT: Microsoft Copilot ↑↑↑
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm


# Create your views here


@login_required
def make_appointment(request):
    """
    Displays and processes the appointment booking form.

    **Functionality**
    - Requires user authentication.
    - On GET request: Presents a blank `AppointmentForm`.
    - On POST request: Validates and processes form data.
    - Checks for appointment time conflicts with the practitioner.
    - Saves the appointment if there's no conflict.
    - Displays relevant success or error messages.

    **Context**
    - `appointment_form`: Instance of `AppointmentForm`.

    **Template**
    - Renders form at :template:`appointments/make_appointment.html`
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
                               "This time slot has already been taken. "
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
    Lists all appointments made by the logged-in user.

    **Functionality**
    - Requires user authentication.
    - Fetches and displays user's appointments, ordered chronologically.

    **Context**
    - `appointments`: Queryset of the user's appointments ordered 
    by date and time.

    **Template**
    - Renders the list at :template:`appointments/my_appointments.html`
    """
    appointments = Appointment.objects.filter(customer=request.user)\
        .order_by('appointment_date', 'time')

    return render(
        request,
        'appointments/my_appointments.html',
        {'appointments': appointments}
    )


def edit_appointment(request, appointment_id):
    """
    Allows the logged-in user to modify an existing appointment.

    **Functionality**
    - Retrieves appointment by `appointment_id` belonging to the current user.
    - On GET request: Pre-populates form with current appointment data.
    - On POST request:
    - Validates updated form.
    - Checks for appointment conflicts excluding current instance.
    - Saves updated appointment if no conflict occurs.
    - Displays appropriate success or error messages.

    **Context**
    - `appointment_form`: Instance of `AppointmentForm`
    tied to the appointment.

    **Template**
    - Renders form at :template:`appointments/edit_appointment.html`
    """
    # ↓↓↓ CREDIT: I think therefore I blog, Code Institute Project ↓↓↓
    appointment = get_object_or_404(
        Appointment, id=appointment_id, customer=request.user)
    appointment_form = AppointmentForm(instance=appointment)

    if request.method == "POST":
        appointment_form = AppointmentForm(request.POST, instance=appointment)
        # ↑↑↑ CREDIT: I think therefore I blog, Code Institute Project ↑↑↑
        if appointment_form.is_valid():
            updated = appointment_form.save(commit=False)
            updated.employee = updated.treatment.practitioner
            conflict = Appointment.objects.filter(
                employee=updated.employee,
                appointment_date=updated.appointment_date,
                time=updated.time
                ).exclude(id=appointment_id).exists()

            if conflict:
                messages.error(
                    request,
                    "This time slot is already taken. Please choose another.")
            else:
                updated.save()
                messages.success(request, "Appointment updated successfully!")
                return redirect('myappointments')

    return render(request,
                  'appointments/edit_appointment.html',
                  {'appointment_form': appointment_form})


@login_required
def cancel_appointment(request, appointment_id):
    """
    Deletes a specific appointment made by the user.

    **Functionality**
    - Requires user authentication.
    - Retrieves appointment via `appointment_id` and deletes it.
    - Displays confirmation message and redirects to the user's 
    appointments list.

    **Template**
    - No template rendered; redirects to :view:`user_appointments`
    """
    appointment = get_object_or_404(Appointment, id=appointment_id,
                                    customer=request.user)
    appointment.delete()
    messages.success(request, "Appointment cancelled successfully!")
    return redirect('myappointments')
