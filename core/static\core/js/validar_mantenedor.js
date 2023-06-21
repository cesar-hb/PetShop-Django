function generarContrasena() {
    var caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.,";
    var longitud = 8; 
    var contrasena = "";
    for (var i = 0; i < longitud; i++) {
      var indice = Math.floor(Math.random() * caracteres.length);
      contrasena += caracteres.charAt(indice);
    }
    password1.innerHTML = contrasena;
  }    
$(document).ready(function() {
    
    $.validator.addMethod("rutChile", function(value, element) {
        // Eliminar puntos y guión del RUT
        value = value.replace(/[.-]/g, "");
    
        // Validar que el RUT tenga 8 o 9 dígitos
        if (value.length < 8 || value.length > 9) {
          return false;
        }
    
        // Validar que el último dígito sea un número o una 'K'
        var validChars = "0123456789K";
        var lastChar = value.charAt(value.length - 1).toUpperCase();
        if (validChars.indexOf(lastChar) == -1) {
          return false;
        }
    
        // Calcular el dígito verificador
        var rut = parseInt(value.slice(0, -1), 10);
        var factor = 2;
        var sum = 0;
        var digit;
        while (rut > 0) {
          digit = rut % 10;
          sum += digit * factor;
          rut = Math.floor(rut / 10);
          factor = factor === 7 ? 2 : factor + 1;
        }
        var dv = 11 - (sum % 11);
        dv = dv === 11 ? "0" : dv === 10 ? "K" : dv.toString();
    
        // Validar que el dígito verificador sea correcto
        return dv === lastChar;
      }, "Por favor ingrese un RUT válido."); 


    $("#formularioMantUser").validate({
      rules: {
        rut:{
            required: true,
            rutChile: true,
            maxlength: 10,
        },
        nombres:{
            required: true,
            minlength: 2,
            maxlength: 25,
        },
        apellidos:{
            required: true,
            minlength: 2,
            maxlength: 25,
        },
        email: {
            required: true,
            email: true,
        },
        direccion:{
            required: true,
            minlength: 5,
            maxlength: 150,
        },
        password1: {
          required: true,
          minlength: 8,
          maxlength: 20,
          value:generarContrasena,
        },

      }, // --> Fin de reglas
      messages: {
        rut:{
            required: "Es obligatorio un RUT correctamente emitido",
            rutChileno: "El formato del rut no es válido",
            maxlength: "10 caracteres maximo"
        },
        nombres:{
            required: "Este campo es obligatorio",
            minlength: "El debe tener al menos 2 carácteres",
            maxlength: "El debe tener a lo más 25 carácteres",
        },
        apellidos:{
            required: "Este campo es obligatorio",
            minlength: "El debe tener al menos 2 carácteres",
            maxlength: "El debe tener a lo más 25 carácteres",
        },
        email: {
            required:"El email es un campo requerido",
            email: "El email no cumple el formato de un correo",
        },
        direccion:{
            required: "Este campo es obligatorio",
            minlength: "El debe tener al menos 5 carácteres",
            maxlength: "El debe tener a lo más 150 carácteres",
        },
        password1: {
            required: "La contraseña es una campo obligatorio",
            minlength: "Mínimo 8 caracteres",
            maxlength: "Máximo 20 caracteres",
        },
      },
    });
     
    $("#guardar").click(function () { 
      if ($("#formularioMantUser").valid()) {
        // El formulario es válido, redirigir al usuario a la página siguiente
        alert("Datos guardados");
        window.location.href = "../mantenedorUsuarios.html";
      } else {
        // El formulario no es válido, mostrar un mensaje de error
        alert("Por favor, completa correctamente los campos obligatorios.");
      }      
    });
    $("#eliminar").click(function () { 
        alert("Datos eliminados");
        window.location.href = "../mantenedorUsusarios.html";
    });
});