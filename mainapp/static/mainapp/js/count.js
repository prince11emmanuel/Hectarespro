function animateCounter(id, target, duration) {
  const element = document.getElementById(id);
  let start = 0;
  const increment = Math.ceil(target / (duration / 30)); // 30ms per frame

  const timer = setInterval(() => {
    start += increment;
    if (start >= target) {
      element.textContent = target;
      clearInterval(timer);
    } else {
      element.textContent = start;
    }
  }, 30); // Update every 30ms
}

// Start counting when the DOM is fully loaded
window.addEventListener("DOMContentLoaded", () => {
  animateCounter("clients-count", 1200, 2000);
  animateCounter("jobs-count", 850, 2000);
  animateCounter("experience-count", 12, 2000);
});
