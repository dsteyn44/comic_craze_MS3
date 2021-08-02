$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.dropdown-trigger').dropdown();
    $('.tooltipped').tooltip();
    $('.datepicker').datepicker({
      format: "dd mmm yyyy",
      yearRange: 100,
      showClearBtn: true,
      i18n: {
          done: "Select"
      }
    });
     $('select').formSelect();
  });

  