$(document).ready(function() {
    $('#contactSubmit').click(function () {
        var name = document.contactForm.name.value;
        var email = document.contactForm.email.value;
        var message = document.contactForm.message.value;
        if(name || email || message === "") {
            $('#emptyField').modal("show");
            return false;
        }
    });
});