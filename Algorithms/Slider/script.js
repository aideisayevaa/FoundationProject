let img=document.querySelector('slide-img img');
let imgSources=[
    'img/1.jpg',
    'img/2.jpg',
    'img/3.jpg'
]

let count=0;
function goPrev(){
    if(count<1){
        img.setAttribute('src',imgSources[2])
        count=2
    }else{
        img.setAttribute('src',imgSources[count])
        count--
    }
}

function goNext(){
    if(count>2){
        img.setAttribute('src',imgSources[0])
        count=0
    }else{
        img.setAttribute('src',imgSources[count])
        count++
    }
}