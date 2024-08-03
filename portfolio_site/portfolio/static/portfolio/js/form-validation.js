// Utility class to handle form validation
class FormValidator {
    // Prevent instantiation of this utility class
    constructor() {
        throw new Error('This class cannot be instantiated');
    }

    // Static method to validate name input
    static nameIsValid(name) {
        return (name.value.trim() !== '' && name.value.length < 100);
    }

    // Static method to validate email input using a regex pattern
    static emailIsValid(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email.value);
    }

    // Static method to validate message input
    static validateMessage(message) {
        return message.value.trim() !== '';
    }
}

// Event listener for when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Select the form and its input elements
    const form = document.getElementById('contact-form');
    const nameInput = form.querySelector('input[name="name"]');
    const emailInput = form.querySelector('input[name="email"]');
    const messageInput = form.querySelector('textarea[name="message"]');

    // Function to reset all form inputs on page reload
    function resetForm() {
        if (form) {
            const inputs = form.querySelectorAll('input, textarea');
            inputs.forEach(input => {
                input.value = '';
            });
        }
    }
    resetForm();

    // Function to validate the name input and update the UI accordingly
    function validateAndRenderName() {
        const nameError = document.getElementById('nameError');
        if (!FormValidator.nameIsValid(nameInput)) {
            nameInput.classList.add('is-invalid');
            nameError.style.display = 'block';
            return false;
        } else {
            nameInput.classList.remove('is-invalid');
            nameError.style.display = 'none';
            return true;
        }
    }

    // Function to validate the email input and update the UI accordingly
    function validateAndRenderEmail() {
        const emailError = document.getElementById('emailError');
        if (!FormValidator.emailIsValid(emailInput)) {
            emailInput.classList.add('is-invalid');
            emailError.style.display = 'block';
            return false;
        } else {
            emailInput.classList.remove('is-invalid');
            emailError.style.display = 'none';
            return true;
        }
    }

    // Function to validate the message input and update the UI accordingly
    function validateAndRenderMessage() {
        const messageError = document.getElementById('messageError');
        if (!FormValidator.validateMessage(messageInput)) {
            messageInput.classList.add('is-invalid');
            messageError.style.display = 'block';
            return false;
        } else {
            messageInput.classList.remove('is-invalid');
            messageError.style.display = 'none';
            return true;
        }
    }

    // Function to validate the entire form on submission
    function validateForm(event) {
        let isValid = true;

        if (!validateAndRenderName()) {
            isValid = false;
        }

        if (!validateAndRenderEmail()) {
            isValid = false;
        }

        if (!validateAndRenderMessage()) {
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault();
        }
    }

    // Attach event listeners to form elements for validation
    form.addEventListener('submit', validateForm);
    nameInput.addEventListener('input', validateAndRenderName);
    emailInput.addEventListener('input', validateAndRenderEmail);
    messageInput.addEventListener('input', validateAndRenderMessage);
});