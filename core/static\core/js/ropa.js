$(document).ready(function() {
    $.get('https://fakestoreapi.com/products',
    function(data) {
        $('#producto').empty();
        $.each(data, function(i, item){
            var contenido = `
            <div class="col-sm-12 col-md-6 col-lg-4 col-xl-3 pad-b">
                <img class="producto" src="` + item.image + `"  alt="">
                <p class="fs-5"> $` + item.price +  `</p> 
                <p><b>` + item.title + `</b><br>
                <b>Descripción:</b>
                ` + item.description +`</p> 
            </div>
            `;
            $('#producto').append(contenido);
        });
    });
});