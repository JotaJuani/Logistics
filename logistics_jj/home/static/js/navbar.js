const navbarEl = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
    if(window.scrollY > 450){
        navbarEl.classList.add('navbar-scrolled');
    } else {
        navbarEl.classList.remove('navbar-scrolled');
    }
});
