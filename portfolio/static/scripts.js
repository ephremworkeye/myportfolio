// alert('hello world');


var header = document.getElementById('nav-menu');
var navLinks = header.getElementsByClassName('nav-link');
// Loop through the buttons and add the active class to the current 
for (var i = 0; i < navLinks.length; i++) {
    navLinks[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}

var typed = new Typed(".auto-input", {
    strings: ["Ephrem Wube", "Full Stack Developer", "Django Developer"],
    typeSpeed: 100,
    backSpeed: 100,
    loop: true
});

// tool tip for banner image
const tooltips = document.querySelectorAll('.tt')
tooltips.forEach(t => {
    new bootstrap.Tooltip(t)
})


// get the current year
const copyRight = document.querySelector('.copy-right');

const d = new Date();
const yearPart = d.getFullYear();

copyRight.textContent = `${yearPart} ephrempro: All rights reserved`;


