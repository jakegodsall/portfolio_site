const carouselWrapper = document.querySelector('.carousel-wrapper');
const carousel = document.querySelector('.carousel');
const projects = document.querySelectorAll('.carousel > li');
const nextBtn = document.querySelector('.next-btn');
const prevBtn = document.querySelector('.prev-btn');

let currentIndex = 0;
const totalProjects = projects.length;
const projectsToShow = 3; // Show 3 slides at a time
const maxIndex = totalProjects - projectsToShow;

console.log(totalProjects)

if (totalProjects < 4) {
  prevBtn.style.display = 'none';
  nextBtn.style.display = 'none';
}

toggleInactiveState(prevBtn, currentIndex, 0);
toggleInactiveState(nextBtn, currentIndex, maxIndex);

nextBtn.addEventListener('click', () => {
  if (currentIndex < maxIndex) {
    currentIndex++;
    updateCarousel();

    toggleInactiveState(prevBtn, currentIndex, 0);
    toggleInactiveState(nextBtn, currentIndex, maxIndex);
  }
});

prevBtn.addEventListener('click', () => {
  if (currentIndex > 0) {
    currentIndex--;
    updateCarousel();

    toggleInactiveState(prevBtn, currentIndex, 0);
    toggleInactiveState(nextBtn, currentIndex, maxIndex);
  }
});

function toggleInactiveState(element, currentIndex, targetIndex) {
    if (currentIndex === targetIndex) {
      element.classList.add("inactive");
    } else {
      element.classList.remove("inactive");
    }
}

function updateCarousel() {
  const totalShift = -(405) * currentIndex; // Slide width + gap (20px)
  carousel.style.transform = `translateX(${totalShift}px)`;
}