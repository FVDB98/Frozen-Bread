document.addEventListener("DOMContentLoaded", () => {

    const mobileMenu = document.getElementById("mobileMenu");
    const hamburger = document.querySelector(".hamburger");
    const closeBtn = document.querySelector(".close-menu");

    // Open menu
    hamburger.addEventListener("click", () => {
        mobileMenu.classList.add("open");
    });

    // Close menu
    closeBtn.addEventListener("click", () => {
        mobileMenu.classList.remove("open");
    });

    // Close menu on link click (optional)
    document.querySelectorAll(".mobile-menu-links a").forEach(link => {
        link.addEventListener("click", () => {
            mobileMenu.classList.remove("open");
        });
    });
});

// MOBILE SLIDESHOW
document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".gallery-slider .slide");
    let index = 0;

    if (slides.length > 0) {
        slides[index].style.display = "block";

        setInterval(() => {
            slides[index].style.display = "none";
            index = (index + 1) % slides.length;
            slides[index].style.display = "block";
        }, 3000);
    }
});

// FAQ accordion
document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".faq-item");

    items.forEach(item => {
        const button = item.querySelector(".faq-question");

        button.addEventListener("click", () => {
            item.classList.toggle("active");
        });
    });
});

// Flash message auto-dismiss
setTimeout(() => {
    document.querySelectorAll(".flash-message").forEach(el => {
        el.style.transition = "0.4s ease";
        el.style.opacity = "0";
        el.style.transform = "translateY(-5px)";
        setTimeout(() => el.remove(), 400);
    });
}, 3000);
