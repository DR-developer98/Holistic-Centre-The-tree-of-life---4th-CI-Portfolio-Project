/**
 * Appointment cancellation modal 
 * 
 * When a user clicks a "Cancel appointment" button on any appointment card,
 * this code:
 *  - Captures the triggering button by means of the click event listener;
 *  - Extracts the appointment-id stored in the button's data-id attribute;
 *  - Dynamically sets the href attribute of the modal's confirmation button (#cancelConfirm)
 *    to point to the correct cancellation URL: /appointments/cancel/<appointment_id>/
 */
document.querySelectorAll('.cancel-btn').forEach(button => {
    button.addEventListener('click', function () {
        const appointmentId = button.getAttribute('data-id');
        const confirmBtn = document.getElementById('cancelConfirm');
        confirmBtn.setAttribute('href', `/appointments/cancel/${appointmentId}/`);
    });
});