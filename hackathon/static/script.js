let searchBtn=document.querySelector('#search-btn');
let searchBar=document.querySelector('.search-bar-container');
let formBtn=document.querySelector('#login-btn');
let loginForm=document.querySelector('.login-form-container');
let formClose=document.querySelector('#form-close');
let menu=document.querySelector('#menu-bar');
let navbar=document.querySelector('.navbar')
let abar=document.querySelector('.accessiblity-images');

window.onscroll=()=>{
    searchBtn.classList.remove('fa-times');
    searchBar.classList.remove('active');
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
    loginForm.classList.remove('active');

}

menu.addEventListener('click',()=>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');

})
searchBtn.addEventListener('click',()=>{
    searchBtn.classList.toggle('fa-times');
    searchBar.classList.toggle('active');

})

formBtn.addEventListener('click',()=>{
    loginForm.classList.add('active');
    
    
})
formClose.addEventListener('click',()=>{
    loginForm.classList.remove('active');

    
})
$(document).ready(function(){
    
    $("a").on('click', function(event) {
  
      
      if (this.hash !== "") {
        
        event.preventDefault();
  
       
        var hash = this.hash;
  
       
        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 800, function(){
  
        
          window.location.hash = hash;
        });
      }
    });
});