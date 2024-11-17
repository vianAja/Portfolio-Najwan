// Typewriter Effect
const nameElement = document.getElementById("name");
const name = "Your Name"; // Replace with your custom name
let index = 0;

function typeWriter() {
    if (index < name.length) {
        nameElement.innerHTML += name.charAt(index);
        index++;
        setTimeout(typeWriter, 150); // Typing speed
    }
}
typeWriter();

// Custom Cursor
const cursor = document.getElementById("custom-cursor");
document.addEventListener("mousemove", (e) => {
    cursor.style.left = e.pageX + "px";
    cursor.style.top = e.pageY + "px";
    cursor.style.transform = "scale(1.2)";
    setTimeout(() => (cursor.style.transform = "scale(1)"), 100);
});

// Particles.js Configuration
particlesJS("particle-container", {
    particles: {
        number: { value: 100, density: { enable: true, value_area: 800 } },
        color: { value: "#ffffff" },
        shape: { type: "circle" },
        opacity: { value: 0.5 },
        size: { value: 5 },
        line_linked: { enable: false },
        move: {
            enable: true,
            speed: 2,
            direction: "none",
            random: true,
            straight: false,
            out_mode: "out",
        },
    },
    interactivity: {
        detect_on: "canvas",
        events: {
            onhover: { enable: true, mode: "repulse" },
            onclick: { enable: true, mode: "push" },
        },
        modes: {
            repulse: { distance: 100 },
            push: { particles_nb: 4 },
        },
    },
    retina_detect: true,
});
