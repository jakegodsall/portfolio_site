const hamburger = document.getElementById("hamburger");

hamburger.addEventListener("click", toggleMenu);

function toggleMenu() {
    const navbarNav = document.getElementById("navbarNav");
    navbarNav.classList.toggle("active");
}