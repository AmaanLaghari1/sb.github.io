let sticky = document.getElementById('navbar')
let hamburger = document.querySelector('.hamburger');
let nav = document.querySelector("nav");


window.addEventListener('scroll', () => {
    if(window.pageYOffset >= 100){
        sticky.classList.add('fixed-top')
        sticky.style.cssText = 'transition: 1s;'
    }
    else if (window.pageYOffset <= 100) {
        sticky.classList.remove('fixed-top')
        sticky.style.cssText = 'background: #0E1116; transition: 1s;'
    }
})
