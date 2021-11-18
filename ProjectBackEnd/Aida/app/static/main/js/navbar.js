var navbar = document.getElementsByClassName('navbar')
var navSec = document.getElementById('myNavbar')
var menu = document.getElementsByClassName('home-li')
window.addEventListener('scroll', () => {
    if (window.scrollY > 500) {
        if (navSec.style.position == 'fixed') return
        console.log(1)
        navSec.style.position = 'fixed'
        navbar[0].style.background = '#1F2D3D'
        navbar[0].style.boxShadow = '0 1px 3px rgb(0 0 0 / 11%)'
        navSec.style.animation = 'appearance 1s ease normal'
        for (let i = 0; i < menu.length; i++) {
            
        }
    } else {

        navSec.style.animation = ''
        for (let i = 0; i < menu.length; i++) {
            menu[i].style.color = ''

        }
        navbar[0].style.background = none
        navbar[0].style.width = '100%'
        navbar[0].style.boxShadow = '0'
    }
})

const typed = select('.typed')
if (typed) {
  let typed_strings = typed.getAttribute('data-typed-items')
  typed_strings = typed_strings.split(',')
  new Typed('.typed', {
    strings: typed_strings,
    loop: true,
    typeSpeed: 100,
    backSpeed: 50,
    backDelay: 2000
  });
}