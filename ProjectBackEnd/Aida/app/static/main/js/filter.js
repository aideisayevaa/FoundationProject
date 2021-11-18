filterSelection('all')
function filterSelection(c) {
    var x, i;
    x = document.getElementsByClassName("portfolio");
    if(c == 'all') {
        for (let i = 0; i < x.length; i++) {
                x[i].style.display= 'block'
                x[i].style.animation = 'zoom-in .7s ease'
        }
        return
    }
    
    for (let i = 0; i < x.length; i++) {
        
        if(!x[i].classList.contains(c)){
            x[i].style.display = 'none'
        } else {
            x[i].style.display = 'block'
        }       
    }
    
}