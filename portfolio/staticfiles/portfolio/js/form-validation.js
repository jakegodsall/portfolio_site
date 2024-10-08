// Utility class to handle form validation
class FormValidator {
    // Prevent instantiation of this utility class
    constructor() {
        throw new Error('This class cannot be instantiated');
    }

    // Static method to validate name input
    static textInputIsValid(name) {
        return (name.value.trim() !== '' && name.value.length < 100);
    }

    // Static method to validate email input using a regex pattern
    static emailInputIsValid(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email.value);
    }

    // Static method to validate message input
    static messageInputIsValid(message) {
        return message.value.trim() !== '';
    }
}

// Event listener for when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Select the form and its input elements
    const form = document.getElementById('contact-form');
    const nameInput = form.querySelector('input[name="name"]');
    const subjectInput = form.querySelector('input[name="subject"]')
    const emailInput = form.querySelector('input[name="email"]');
    const messageInput = form.querySelector('textarea[name="message"]');

    // Function to reset all form inputs on page reload
    function resetForm() {
        if (form) {
            // inputs not including hidden CSRF token input
            const inputs = form.querySelectorAll('input:not([name=csrfmiddlewaretoken]), textarea');
            inputs.forEach(input => {
                input.value = '';
            });
        }
    }
    resetForm();

    // Function to validate the name input and update the UI accordingly
    function validateAndRenderName() {
        const nameError = document.getElementById('nameError');
        if (!FormValidator.textInputIsValid(nameInput)) {
            nameInput.classList.add('is-invalid');
            nameError.classList.add('active');
            return false;
        } else {
            nameInput.classList.remove('is-invalid');
            nameError.classList.remove('active');
            return true;
        }
    }

    // Function to validate the subject input and update the UI accordingly
    function validateAndRenderSubject() {
        const subjectError = document.getElementById('subjectError');

        if (!FormValidator.textInputIsValid(nameInput)) {
            subjectInput.classList.add('is-invalid');
            subjectError.classList.add('active');
            return false;
        } else {
            subjectInput.classList.remove('is-invalid');
            subjectError.classList.remove('active');
            return true;
        }
    }

    // Function to validate the email input and update the UI accordingly
    function validateAndRenderEmail() {
        const emailError = document.getElementById('emailError');
        if (!FormValidator.emailInputIsValid(emailInput)) {
            emailInput.classList.add('is-invalid');
            emailError.classList.add('active')
            return false;
        } else {
            emailInput.classList.remove('is-invalid');
            emailError.classList.remove('active');
            return true;
        }
    }

    // Function to validate the message input and update the UI accordingly
    function validateAndRenderMessage() {
        const messageError = document.getElementById('messageError');
        if (!FormValidator.messageInputIsValid(messageInput)) {
            messageInput.classList.add('is-invalid');
            messageError.classList.add('active');
            return false;
        } else {
            messageInput.classList.remove('is-invalid');
            messageError.classList.remove('active');
            return true;
        }
    }

    // Function to validate the entire form on submission
    function validateForm(event) {
        let isValid = true;

        // Perform validation checks
        if (!validateAndRenderName()) isValid = false;
        if (!validateAndRenderSubject()) isValid = false;
        if (!validateAndRenderEmail()) isValid = false;
        if (!validateAndRenderMessage()) isValid = false;

        // If the form is not valid, prevent submission
        if (!isValid) {
            event.preventDefault(); // Stops the form from submitting if validation fails
        }
        // If the form is valid, the form will submit naturally, and the CSRF token will be included automatically
    }

    // Attach event listeners to form elements for validation
    form.addEventListener('submit', validateForm);
    nameInput.addEventListener('input', validateAndRenderName);
    subjectInput.addEventListener('input', validateAndRenderSubject);
    emailInput.addEventListener('input', validateAndRenderEmail);
    messageInput.addEventListener('input', validateAndRenderMessage);
});