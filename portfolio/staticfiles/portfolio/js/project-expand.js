const projectDetails = document.querySelectorAll(".project-detail");
console.log(projectDetails);

projectDetails.forEach(projectDetail => {
   const caretToggle = projectDetail.querySelector("#caret-toggle");
   console.log(caretToggle);

   // Attach event listener to toggle the visibility of the .project-content
    caretToggle.addEventListener('click', () => {
        // Toggle the display of the .project-content
        caretToggle.classList.toggle('active');
        const content = projectDetail.querySelector('.project-detail_extended-content');
        content.classList.toggle('open');
      });
});