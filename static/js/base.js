// Top of page JS inspired by w3schools and adapted to my needs
window.onscroll = function () {
    pageScroll()
};

// show/hide button depending on where user is in document.
function pageScroll() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("topPageBtn").style.display = "block";
    } else {
        document.getElementById("topPageBtn").style.display = "none";
    }
}

// scroll to top of page when user clicks on button
function topOfPage() {
    document.body.scrollTop = 0; // Safari
    document.documentElement.scrollTop = 0; // Chrome, Firefox, IE and Opera.
}