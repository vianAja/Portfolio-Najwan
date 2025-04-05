
// <script src="https://cdn.emailjs.com/dist/email.min.js"></script>

  // Inisialisasi EmailJS (gunakan user ID dari EmailJS dashboard)
document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM loaded"); // ini harus muncul di console
    
    emailjs.init({
        publicKey: '1sSPJPcY6tnPF7wth',
        // Do not allow headless browsers
        blockHeadless: true,
        blockList: {
            // Block the suspended emails
            list: ['foo@emailjs.com', 'bar@emailjs.com'],
            // The variable contains the email address
            watchVariable: 'userEmail',
        },
        limitRate: {
            // Set the limit rate for the application
            id: 'app',
            // Allow 1 request per 10s
            throttle: 10000,
        },
    }); // Ganti dengan user ID kamu dari EmailJS
})();

    document.getElementById("contact-form").addEventListener("submit", function(e) {
    e.preventDefault();
    
    console.log("Form submitted"); // ini juga harus muncul

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const subject = document.getElementById("subject").value;
    const message = document.getElementById("message").value;

    const templateParams = {
        from_name: name,
        from_email: email,
        subject: subject,
        message: message
    };

    emailjs.send('service_cgyv113', 'template_visp1hi', templateParams)
        .then(function(response) {
            alert("Email sent successfully!");
        }, function(error) {
            alert("Failed to send email. Please try again.");
            console.error(error);
        });
    });
