// Scroll animation
window.addEventListener("scroll", () => {
  const reveals = document.querySelectorAll(".feature-item");
  for (let i = 0; i < reveals.length; i++) {
    const windowHeight = window.innerHeight;
    const revealTop = reveals[i].getBoundingClientRect().top;
    const revealPoint = 100;
    if (revealTop < windowHeight - revealPoint) {
      reveals[i].classList.add("animate__animated", "animate__fadeInUp");
    }
  }
});
