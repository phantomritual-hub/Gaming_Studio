const contactBtn = document.getElementById("contactBtn");

const popup = document.getElementById("popup");

const closeBtn = document.getElementById("closeBtn");


// OPEN POPUP

contactBtn.addEventListener("click", function() {

    popup.classList.add("active");

});


// CLOSE POPUP

closeBtn.addEventListener("click", function() {

    popup.classList.remove("active");

});


// CLOSE WHEN CLICKING OUTSIDE POPUP

popup.addEventListener("click", function(event) {

    if (event.target === popup) {

        popup.classList.remove("active");

    }

});