/**
 * Appointment cancellation modal 
 * 
 * When a user clicks a "Cancel appointment" button on any appointment card,
 * this script:
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

/**
 * Automatically fades out Django messages after a short delay.
 * 
 * This script:
 * - Waits 4 seconds after page load
 * - Applies Bootstrap's fade and show classes to trigger transition
 * - Then removes the 'show' class after 0.5 seconds to begin fading out 
 * 
 * ↓↓↓ CREDIT: stackoverflow.com ↓↓↓
 */
setTimeout(function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
      alert.classList.add('fade-out');
      setTimeout(() => {
        alert.remove();
      }, 500);
    });
  }, 4000); 