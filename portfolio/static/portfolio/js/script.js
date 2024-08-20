document.getElementById("hamburger").addEventListener("click", function(event) {
     const mobileMenu = document.getElementById("mobile-menu");
     const hamburger = document.getElementById("hamburger");
     mobileMenu.classList.toggle("active");
     hamburger.classList.toggle("active");
})

document.getElementById("mobile-menu").addEventListener("click", function(event) {
    const mobileMenu = document.getElementById("mobile-menu");
    const hamburger = document.getElementById("hamburger");
    if (event.target === mobileMenu) {
        mobileMenu.classList.remove("active");
        hamburger.classList.remove("active");
    }
});

document.getElementById('explore-btn').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('projects').scrollIntoView({ behavior: 'smooth' });
});