document.getElementById('explore-btn').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('projects').scrollIntoView({ behavior: 'smooth' });
});