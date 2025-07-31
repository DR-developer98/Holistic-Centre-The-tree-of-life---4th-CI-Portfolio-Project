/**
 * Appointment cancellation modal 
 * 
 * This code listens for the Bootstrap 'show.bs.modal' event triggered when
 * the appointment cancellation modal (#cancelModal) is about to be shown.
 * 
 * When a user clicks a "Cancel appointment" button on any appointment card,
 * this code:
 *  - Captures the triggering button by means of 'e.relatedTarget';
 *  - Extracts the appointment-id stored in the button's data-id attribute;
 *  - Dynamically sets the href attribute of the modal's confirmation button (#cancelConfirm)
 *    to point to the correct cancellation URL: /appointments/cancel/<appointment_id>/
 */
const cancelModal = document.getElementById('cancelModal');
// ↓↓↓ CREDIT for the show.bs.modal event --> https://www.tutorialspoint.com/Bootstrap-show-bs-modal-Event ↓↓↓
cancelModal.addEventListener('show.bs.modal', function (e) {
    // ↑↑↑ CREDIT for the show.bs.modal event --> https://www.tutorialspoint.com/Bootstrap-show-bs-modal-Event ↑↑↑
    // ↓↓↓ CREDIT: e.relatedTarget https://getbootstrap.com/docs/4.0/components/modal/ ↓↓↓
    const triggerButton = e.relatedTarget;
    // ↑↑↑ CREDIT: e.relatedTarget https://getbootstrap.com/docs/4.0/components/modal/ ↑↑↑
    const appointmentId = triggerButton.getAttribute('data-id');
    const confirmBtn = document.getElementById('cancelConfirm');
    confirmBtn.setAttribute('href', `/appointments/cancel/${appointmentId}/`);
  });