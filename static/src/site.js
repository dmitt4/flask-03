let buttonMenu = document.querySelector('.header .button-menu');
let header = document.querySelector('.header');
let buttonSearch = document.querySelector('.header .bx-search');
let buttonLogout = document.querySelector('.header .button-logout')

buttonMenu.onclick = function() {
  header.classList.toggle('active');
};

buttonSearch.onclick = function() {
  header.classList.toggle('active');
};

buttonLogout.onclick = function() {
  header.classList.toggle('active');
};