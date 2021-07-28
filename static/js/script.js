$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.dropdown-trigger').dropdown();
    $('.tooltipped').tooltip();
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

  