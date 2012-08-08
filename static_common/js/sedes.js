$(document).ready(inicio);

var mapa;
var autocomplete;
var popup;
var infoWindow;

function inicio()
{
	iniciarMapa( document.getElementById('mapa') );
}

function iniciarMapa(mapDiv)
{
   	var opciones = {
    	zoom: 6,
    	center: new google.maps.LatLng(4.520855,-74.098308),
    	mapTypeId: google.maps.MapTypeId.ROADMAP
	};

	mapa = new google.maps.Map( mapDiv, opciones );
    infoWindow = new google.maps.InfoWindow;
	
    getData();
    setAutoComplete();
}

function setAutoComplete()
{
    var options = {
        types: ['(cities)','(regions)'],
        componentRestrictions: {country: 'co'}
    };

    var input = document.getElementById('input_search');
    autocomplete = new google.maps.places.Autocomplete(input, options);
      
    google.maps.event.addListener(autocomplete, 'place_changed', alCambiarInput );
}

    function alCambiarInput()
    {
        var place = autocomplete.getPlace();

        if (place.geometry.viewport) {
            mapa.fitBounds(place.geometry.viewport);
        } else {
            mapa.setZoom(16);  // Why 16? Because it looks good.
        }
    }

function getData()
{
    $.ajax({  
       type: "GET",
       url:"/sedes/",
       dataType : 'json',
       success: respuesta,
       error: alError
    });
}

function respuesta(data)
{
    var sede;

    for (var i in data )// = 0; i < data.length; i++) 
    {
        sede = data[i]['fields'];       
        setMarkerts(sede);
    } 
}

function setMarkerts(sede)
{
    var point = sede.geolocation.split(',');
    var latlng = new google.maps.LatLng( parseFloat(point[0]), parseFloat(point[1]) );

    var marker = new google.maps.Marker({
        position: latlng
        , map: mapa
        , title: sede.alias
        , icon: 'http://gmaps-samples.googlecode.com/svn/trunk/markers/red/marker1.png'
    });

    var html = '<h3>Iglesia Alianza Cristiana - '+sede.codigo+'</h3>';
    html += '<b>Sede: </b>'+sede.alias+' / '+ sede.address+'<br/>';
    if(sede.pastor){
       html += '<b>Pastor: </b>'+sede.pastor+'<br/>'; 
    }
    if(sede.direccion){
       html += '<b>Dirección: </b>'+sede.direccion+'<br/>'; 
    }
    if(sede.web){
       html += '<a href="'+sede.web+'">Más información</a>'; 
    }
    

    bindInfoWindow(marker, html);
}

function bindInfoWindow(marker, html) 
{
  google.maps.event.addListener(marker, 'click', function() {
    infoWindow.setContent(html);
    infoWindow.open(mapa, marker);
  });
}

function alError(e)
{
    alert('Falló el servidor: '+e.error);
}


function crearMarcadores()
{
	var n = 1;
	for(var i in place){
        var marker = new google.maps.Marker({
            position: 1
            , map: mapa
            , title: i
            , icon: 'http://gmaps-samples.googlecode.com/svn/trunk/markers/red/marker' + n++ + '.png'
        });
    
	    google.maps.event.addListener(marker, 'mouseover', function(){
	    	if(!popup){
                popup = new google.maps.InfoWindow();
            }
            var note = 'Iglesia: ' + this.title;
            popup.setContent(note);
            popup.open(mapa, this);
	    });
	}
}



function abrirVentana()
{
	var popup = new google.maps.InfoWindow({
        content: 'Soy la ventana'
    });
 
    popup.open(mapa, marker);
}

$(document).ajaxStart(function(){
    $('#spinner').show();
}).ajaxStop(function(){
    $('#spinner').hide();
});



//// ESTO ANALIZA SI SE RECIBIO LA COKIE Y LA DEVUELVA AL SERVIDOR ///////////////////

$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
}); 
