//  Inspired by Stack Overflow post and expanded upon, listed in credits.
function alternativeImage(image) {
    image.onerror = "";
    image.src = "https://placehold.it/100";
    return true;
}