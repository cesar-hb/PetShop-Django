// Cargar navbar y footer usando el raw de github con el menú.
// No me funciono haciendo dos funciones distintas, así que anidé los dos request en uno solo.

let request = new XMLHttpRequest();
request.open('GET', 'https://raw.githubusercontent.com/cesar-hb/PetShop-Django/main/core/templates/core/menu.html');
request.send(document.body);
request.onload = function() {
  let contenido = request.response;
  $('#navbar-div').append(contenido);
  request.open('GET', 'https://raw.githubusercontent.com/cesar-hb/PetShop-Django/main/core/templates/core/footer.html');
  request.send(document.body);
  request.onload = function() {
    let contenido = request.response;
    $('#footer').append(contenido);
    };
};
