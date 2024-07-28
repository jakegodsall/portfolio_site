const hamburger = document.getElementById("hamburger");

hamburger.addEventListener("click", toggleMobileMenu);

function toggleMobileMenu() {
    const mobileMenu = document.getElementById("mobile-menu");
    mobileMenu.classList.toggle("active");
}