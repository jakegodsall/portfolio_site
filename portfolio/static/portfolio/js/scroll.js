document.getElementById('explore-btn').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('project-section').scrollIntoView({ behavior: 'smooth' });
});

document.getElementById('projects-link').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('project-section').scrollIntoView({ behavior: 'smooth' });
});

document.getElementById('contact-link').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('contact-section').scrollIntoView({ behavior: 'smooth' });
});

