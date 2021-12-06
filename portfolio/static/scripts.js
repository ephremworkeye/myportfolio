// alert('hello world');

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

