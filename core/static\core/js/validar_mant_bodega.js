$(document).ready(function() {
    $.validator.addMethod("aceptarDigitos", function(value, element) {
      if(isNaN(parseFloat(value)) == false){
        return true;
      }
      return false;
    },"Por favor escribir sólo números.");

    $.validator.addMethod("minimoPrecio", function(value, element) {
      let valor = parseFloat(value);
      if(valor < 0){
        return false;
      }
      return true;
    },"La cantidad no puede ser menor a 0.");
      $("#formularioMantBodega").validate({
        rules: {
          categoria:{
            required: true,
          },
          nombre:{
            required: true,
          },
          descripcion:{
            required: true,
            minlength: 2,
            maxlength: 200,
          },
          cantidad:{
            required: true,
            maxlength:6,
            aceptarDigitos: true,
            minimoPrecio:true,
          },
  
        }, // --> Fin de reglas
        messages: {
          categoria:{
            required: "Este campo es obligatorio",
          },
          nombre:{
            required: "Este campo es obligatorio",
          },
          descripcion:{
            required: "Este campo es obligatorio",
            minlength: "El debe tener al menos 2 carácteres",
            maxlength: "El debe tener a lo más 200 carácteres",
          },
          cantidad:{
            required: "Este campo es obligatorio",
            maxlength: "Cantidad exedida, numero hasta 6 digitos",
            aceptarDigitos: "Numero mal escrito",
            minimoPrecio: "La cantidad no puede ser menor a 0.",
          },
        },
      });
      $("#agregar").click(function () { 
        if ($("#formularioMantBodega").valid()) {
          // El formulario es válido, redirigir al usuario a la página siguiente
          alert("Datos guardados");
          window.location.href = "../mantenedorBodega.html";
        } else {
          // El formulario no es válido, mostrar un mensaje de error
          alert("Por favor, completa correctamente los campos obligatorios.");
        }      
      });
  });