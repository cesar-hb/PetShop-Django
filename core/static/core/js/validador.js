$(document).ready(function() {

 
    $("#formularioIngreso").validate({
      rules: {
        email: {
          required: true,
          email: true,
        },
        password1: {
          required: true,
          minlength: 8,
          maxlength: 20,
        },
      }, // --> Fin de reglas
      messages: {
        email: {
          required:"El email es un campo requerido",
          email: "El email no cumple el formato de un correo",
        },
        password1: {
          required: "La contraseña es una campo obligatorio",
          minlength: "Mínimo 8 caracteres",
          maxlength: "Máximo 20 caracteres",
        },
      },
    });
    $("#ingresar").click(function () { 
      if ($("#formularioIngreso").valid()) {
        // El formulario es válido, redirigir al usuario a la página siguiente
        let email = $("#email").val();
        window.location.href = "inicioCliente.html";
      } else {
        // El formulario no es válido, mostrar un mensaje de error
        alert("Por favor, completa correctamente los campos obligatorios.");
      }      
    });
});