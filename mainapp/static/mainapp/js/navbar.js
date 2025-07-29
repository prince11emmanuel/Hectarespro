document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("nav-toggle");
    const navLinks = document.getElementById("nav-links");

    toggleBtn.addEventListener("click", () => {
        navLinks.classList.toggle("open");
    });
});


