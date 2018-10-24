//  Inspired by Stack Overflow post and expanded upon, listed in credits.
function alternativeImage(image) {
    image.onerror = "";
    image.src = "https://thepchobbyist.s3.amazonaws.com/static/img/default_avatar.jpg";
    return true;
}