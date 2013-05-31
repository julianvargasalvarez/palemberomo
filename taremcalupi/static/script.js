$(function(){

  $("a").on("click", function(){
    return confirm("are you sure you want to remove this?");
  });

  $(".pejemaneje").css({'width': '400px', 'height': '400px'}).load('http://www.eltiempo.com/', function(){
        alert("listo");
      });  
});
