$(document).ready(function(){
    $('.carousel').carousel();
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.dropdown-trigger').dropdown();
    $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      yearRange: 100,
      showClearBtn: true,
      i18n: {
          done: "Select"
      }
    });
     $('select').formSelect();
  });