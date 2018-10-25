$(document).ready(function () {

    var imgModalOne = document.getElementById('imgModal-one');
    var imgOne = document.getElementById('imgOne');
    var firstImage = document.getElementById('firstImage');
    var captionOne = document.getElementById('imgModal-captionOne');

    imgOne.onclick = function () {
        imgModalOne.style.display = "block";
        firstImage.src = "https://thepchobbyist.s3.amazonaws.com/static/img/computer_one.jpg";
        captionOne.innerHTML = this.alt;
    }

    var imgModalTwo = document.getElementById('imgModal-two');
    var imgTwo = document.getElementById('imgTwo');
    var secondImage = document.getElementById('secondImage');
    var captionTwo = document.getElementById('imgModal-captionTwo');

    imgTwo.onclick = function () {
        imgModalTwo.style.display = "block";
        secondImage.src = "https://thepchobbyist.s3.amazonaws.com/static/img/gaming_competition.jpg";
        captionTwo.innerHTML = this.alt;
    }

    var closeSpanOne = document.getElementById("imgModalOne-close")
    closeSpanOne.onclick = function () {
        imgModalOne.style.display = "none";
    }

    var closeSpanTwo = document.getElementById("imgModalTwo-close")
    closeSpanTwo.onclick = function () {
        imgModalTwo.style.display = "none";
    }
});