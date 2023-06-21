$(document).ready(function() {
  $.validator.addMethod("aceptarDigitos", function(value, element) {
    if(isNaN(parseFloat(value)) == false){
      return true;
    }
    return false;
  },"Por favor escribir sólo números.");
  $.validator.addMethod("maxDescuentSub", function(value, element) {
    let valor = parseFloat(value);
    if(valor < 0 || valor > 5 ){
      return false;
    }
    return true;
  },"Por favor no superar mas de 5%.");
  $.validator.addMethod("maxDescuento", function(value, element) {
    let desc = parseFloat(value);
    if(desc < 0 || desc > 50 ){
      return false;
    }
    return true;
  },"Por favor no superar mas de 50%.");
  $.validator.addMethod("minimoPrecio", function(value, element) {
    let valor = parseFloat(value);
    if(valor < 0){
      return false;
    }
    return true;
  },"El precio no puede ser menor a 0.");
    $("#formularioMantDatos").validate({
      rules: {
        categoria:{
          required: true,
        },
        nombre:{
          required: true,
          minlength: 2,
          maxlength: 30,
        },
        descripcion:{
          required: true,
          minlength: 2,
          maxlength: 200,
        },
        precio:{
          required: true,
          maxlength:10,
          aceptarDigitos: true,
          minimoPrecio:true,
        },
        desc_subscriptor:{
          required: true,
          aceptarDigitos: true,
          maxDescuentSub: true,
        },
        desc_oferta:{
          required: true,
          aceptarDigitos: true,
          maxDescuento: true,
        },

      }, // --> Fin de reglas
      messages: {
        categoria:{
          required: "Este campo es obligatorio",
        },
        nombre:{
          required: "Este campo es obligatorio",
          minlength: "El debe tener al menos 2 carácteres",
          maxlength: "El debe tener a lo más 25 carácteres",
        },
        descripcion:{
          required: "Este campo es obligatorio",
          minlength: "El debe tener al menos 2 carácteres",
          maxlength: "El debe tener a lo más 200 carácteres",
        },
        precio:{
          required: "Este campo es obligatorio",
          maxlength: "Precio exedido, numero hasta 10 digitos",
          aceptarDigitos: "Numero mal escrito",
          minimoPrecio: "El precio no puede ser menor a 0.",
        },
        desc_subscriptor:{
          required: "Este campo es obligatorio",
          aceptarDigitos: "Numero mal escrito",
          maxDescuentSub: "El porcentaje debe estar entre el 0 y el 5%",
        },
        desc_oferta:{
          required: "Este campo es obligatorio",
          aceptarDigitos: "Numero mal escrito",
          maxDescuento: "El porcentaje debe estar entre el 0 y el 50%",
        },
      },
    });
    $("#guardar").click(function () { 
      if ($("#formularioMantDatos").valid()) {
        // El formulario es válido, redirigir al usuario a la página siguiente
        alert("Datos guardados");
        window.location.href = "../mantenedorProductos.html";
      } else {
        // El formulario no es válido, mostrar un mensaje de error
        alert("Por favor, completa correctamente los campos obligatorios.");
      }      
    });
});