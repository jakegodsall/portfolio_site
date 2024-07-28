document.getElementById("hamburger").addEventListener("click", function(event) {
     const mobileMenu = document.getElementById("mobile-menu");
     mobileMenu.classList.toggle("active");
     hamburger.classList.toggle("active");
})

document.getElementById("mobile-menu").addEventListener("click", function(event) {
    const mobileMenu = document.getElementById("mobile-menu");
    if (event.target === mobileMenu) {
        mobileMenu.classList.remove("active");
        hamburger.classList.remove("active");
    }
});