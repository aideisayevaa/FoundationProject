let box=document.querySelector('.box');
let pos=0;
function moveRight(){
    box.style.left=`${pos}px`
    pos+=100;
}

function moveLeft(){
    box.style.left=`${pos}px`
    pos-=100;
}