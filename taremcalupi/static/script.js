$(function(){
  $(".eliminar").on("click", function(){
    $('#myModal').modal();
    return false;
    //return confirm("are you sure you want to remove this?");
  });
  setInterval(getData, 1000);
});

function getData() {
  var exito = function(oskar) {
    $(oskar).each(function(i, usuario){
        var $usr = $('<li/>');
        
        $usr.data('user-id', usuario.pk);
        $usr.attr('id', usuario.pk);
        $usr.text(usuario.fields.email);

        var $ul_usuarios = $("#lista-de-usuarios");

        var $mi_yo_anterior = $("#" + usuario.pk);
        if(!$mi_yo_anterior.length) {
            $ul_usuarios.append($usr);
        }
    });
  }

  var error = function(el_error){
    console.log(el_error);
  }

  $.getJSON('/users_as_json', exito, error);
}
