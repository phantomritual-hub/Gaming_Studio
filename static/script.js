
// ==================================
// CONTACT MODAL
// ==================================

const modal = document.getElementById("contactModal");

const contactButtons = [
    document.getElementById("heroContact"),
    document.getElementById("navContact"),
    document.getElementById("footerContact")
];

const closeButton = document.getElementById("modalClose");

const okayButton = document.getElementById("okayButton");


function openModal() {

    modal.classList.add("active");

    document.body.style.overflow = "hidden";

    okayButton.focus();

}


function closeModal() {

    modal.classList.remove("active");

    document.body.style.overflow = "";

}


contactButtons.forEach(button => {

    button.addEventListener("click", openModal);

});


closeButton.addEventListener("click", closeModal);

okayButton.addEventListener("click", closeModal);


modal.addEventListener("click", event => {

    if (event.target === modal) {

        closeModal();

    }

});


document.addEventListener("keydown", event => {

    if (event.key === "Escape" && modal.classList.contains("active")) {

        closeModal();

    }

});


// ==================================
// MOBILE NAVIGATION
// ==================================

const menuToggle = document.getElementById("menuToggle");

const navLinks = document.getElementById("navLinks");


menuToggle.addEventListener("click", () => {

    const isOpen = navLinks.classList.toggle("active");

    menuToggle.setAttribute("aria-expanded", isOpen);

});


document.querySelectorAll(".nav-links a").forEach(link => {

    link.addEventListener("click", () => {

        navLinks.classList.remove("active");

        menuToggle.setAttribute("aria-expanded", "false");

    });

});


// ==================================
// BACK TO TOP
// ==================================

const floatingTop = document.getElementById("floatingTop");


window.addEventListener("scroll", () => {

    if (window.scrollY > 450) {

        floatingTop.classList.add("visible");

    } else {

        floatingTop.classList.remove("visible");

    }

});


floatingTop.addEventListener("click", () => {

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

});


// ==================================
// FOOTER YEAR
// ==================================

document.getElementById("year").textContent =

    new Date().getFullYear();