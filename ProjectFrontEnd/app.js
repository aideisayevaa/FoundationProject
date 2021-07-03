/* Slider section start */
let imgSlider = document.querySelector(".slide-background img")
imagesSlider = [
    'img/silder1.jpg',
    'img/slider2.jpg',
    'img/slider3.jpg'
]

let countSlider=0;
function goPrev(){
    if(countSlider<2){
        imgSlider.setAttribute('src',imagesSlider[2])
        countSlider++
    }else{
        imgSlider.setAttribute('src',imagesSlider[countSlider-1])
        countSlider--
    }
}

function goNext(){
    if(countSlider>2){
        imgSlider.setAttribute('src',imagesSlider[0])
        countSlider=0
    }else{
        imgSlider.setAttribute('src',imagesSlider[countSlider])
        countSlider++
    }
}

intervalCountSlider=0;
let intervalSlider=setInterval(function(){
   if(intervalCountSlider==3){
       intervalCountSlider=0
   }else{
    imgSlider.setAttribute('src',imagesSlider[intervalCountSlider])
    intervalCountSlider++
   }
},3000)

/* Slider section end */

/* About section start */

let imgAboutRight = document.querySelector(".about-photo-right img")
imagesAboutRight = [
    'img/about01.jpg',
    'img/about02 (1).jpg',
    'img/about03.jpg'
]

intervalCountAboutRight=0;
let intervalAboutRight=setInterval(function(){
   if(intervalCountAboutRight==3){
       intervalCountAboutRight=0
   }else{
    imgAboutRight.setAttribute('src',imagesAboutRight[intervalCountAboutRight])
    intervalCountAboutRight++
   }
},3000)


let imgAboutLeft = document.querySelector(".about-photo-left img")
imagesAboutLeft = [
    'img/about04.jpg',
    'img/about05 (1).jpg',
    'img/about06.jpg'
]

intervalCountAboutLeft=0;
let intervalAboutLeft=setInterval(function(){
   if(intervalCountAboutLeft==3){
       intervalCountAboutLeft=0
   }else{
    imgAboutLeft.setAttribute('src',imagesAboutLeft[intervalCountAboutLeft])
    intervalCountAboutLeft++
   }
},3000)

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


