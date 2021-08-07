let red=document.querySelector('.btnRed')
let blue=document.querySelector('.btnBlue')
let purple=document.querySelector('.btnPurple')

let containerBackground=document.querySelector('.myContainer')

function redBackground(){
    containerBackground.style.background='red'
}

function blueBackground(){
    containerBackground.style.background='blue'
}

function purpleBackground(){
    containerBackground.style.background='purple'
}

red.addEventListener('click',function(){
    redBackground()
})

blue.addEventListener('click',function(){
    blueBackground()
})

purple.addEventListener('click',function(){
    purpleBackground()
})