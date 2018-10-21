$(document).ready(function () {

    $('#contactSubmit').click(function (event) {
        if (document.contactForm.name.value === "") {
            $('#emptyField').modal("show");
            event.preventDefault()
        } else if (document.contactForm.email.value === "") {
            $('#emptyField').modal("show");
            event.preventDefault()
        } else if (document.contactForm.message.value === "") {
            $('#emptyField').modal("show");
            event.preventDefault()
        }
    });
});