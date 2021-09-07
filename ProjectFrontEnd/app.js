



/* Slider section start */
let imgSlider = document.querySelector(".slide-background img")
imagesSlider = [
    'img/silder1.jpg',
    'img/slider2.jpg',
    'img/slider3.jpg'
]

let descSlider = document.querySelector('.slc-welcomeText h2')
descsSlider = [
    'Welcome to restaurant',
    'Elixir exclusively food',
    'The soul food & bistro'
]

let countSlider = 0;

function goPrev() {
    if (countSlider < 2) {
        imgSlider.setAttribute('src', imagesSlider[2])
        countSlider++
    } else {
        imgSlider.setAttribute('src', imagesSlider[countSlider - 1])
        countSlider--
    }
}

function goNext() {
    if (countSlider > 2) {
        imgSlider.setAttribute('src', imagesSlider[0])
        countSlider = 0
    } else {
        imgSlider.setAttribute('src', imagesSlider[countSlider])
        countSlider++
    }
}

intervalCountSlider = 0;
let intervalSlider = setInterval(function () {
    if (intervalCountSlider == 3) {
        intervalCountSlider = 0
    } else {
        imgSlider.setAttribute('src', imagesSlider[intervalCountSlider])
        descSlider.innerHTML = descsSlider[intervalCountSlider]
        intervalCountSlider++
    }
}, 3000)

/* Slider section end */

/* Text */
    const txts = document.querySelector(".slc-welcomeText").children,
    txtsLen = txts.length;
    let index = 0;
    const textInTimer = 3000,
    textOutTimer = 2000;

function animateText() {
    for (let i = 0; i < txtsLen; i++) {
        txts[i].classList.remove("text-in", "text-out");
    }
    txts[index].classList.add("text-in");

    setTimeout(function () {
        txts[index].classList.add("text-out");
    }, textOutTimer)

    setTimeout(function () {

        if (index == txtsLen - 1) {
            index = 0;
        } else {
            index++;
        }
        animateText();
    }, textInTimer);
}

window.onload = animateText;


/* About section start */

let imgAboutRight = document.querySelector(".about-photo-right img")
imagesAboutRight = [
    'img/about01.jpg',
    'img/about02 (1).jpg',
    'img/about03.jpg'
]

intervalCountAboutRight = 0;
let intervalAboutRight = setInterval(function () {
    if (intervalCountAboutRight == 3) {
        intervalCountAboutRight = 0
    } else {
        imgAboutRight.setAttribute('src', imagesAboutRight[intervalCountAboutRight])
        intervalCountAboutRight++
    }
}, 3000)


let imgAboutLeft = document.querySelector(".about-photo-lr=eft img")
imagesAboutLeft = [
    'img/about04.jpg',
    'img/about05 (1).jpg',
    'img/about06.jpg'
]

intervalCountAboutLeft = 0;
let intervalAboutLeft = setInterval(function () {
    if (intervalCountAboutLeft == 3) {
        intervalCountAboutLeft = 0
    } else {
        imgAboutLeft.setAttribute('src', imagesAboutLeft[intervalCountAboutLeft])
        intervalCountAboutLeft++
    }
}, 3000)

/* About section end */

/* Testimonials section start */

var slideIndex = 1;
showSlides(slideIndex);


function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("testimonials-item");
    var dots = document.getElementsByClassName("testimonials-circle");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" testimonials-circle-active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " testimonials-circle-active";
}


/* Gallery filter start */

filterSelection("all")

function filterSelection(c) {
    var x, i;
    x = document.getElementsByClassName("gallery-photo");
    if (c == "all") c = "";
    for (i = 0; i < x.length; i++) {
        removeClass(x[i], "gallery-show");
        if (x[i].className.indexOf(c) > -1) addClass(x[i], "gallery-show");
    }
}

function addClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) {
            element.className += " " + arr2[i];
        }
    }
}

function removeClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
            arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
    }
    element.className = arr1.join(" ");
}

