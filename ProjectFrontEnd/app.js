let img = document.querySelector(".slide-background img")
images = [
    'img/silder1.jpg',
    'img/slider2.jpg',
    'img/slider3.jpg'
]

let count=0;
function goPrev(){
    if(count<2){
        img.setAttribute('src',images[2])
        count++
    }else{
        img.setAttribute('src',images[count-1])
        count--
    }
}

function goNext(){
    if(count>2){
        img.setAttribute('src',images[0])
        count=0
    }else{
        img.setAttribute('src',images[count])
        count++
    }
}


a=0;
let interval=setInterval(function(){
   if(a==3){
       a=0
   }else{
    img.setAttribute('src',images[a])
    a++
   }
},3000)
