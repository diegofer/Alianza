
/*
Integration for Google Maps in the django admin.

How it works:

You have an address field on the page.
Enter an address and an on change event will update the map
with the address. A marker will be placed at the address.
If the user needs to move the marker, they can and the geolocation
field will be updated.

Only one marker will remain present on the map at a time.

This script expects:

<input type="text" name="address" id="id_address" />
<input type="text" name="geolocation" id="id_geolocation" />

<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?libraries=places&sensor=false"></script>

*/

$(document).ready(inicio);

var mapa;
var autocomplete;
var marker;
var location;
var latlng;

var lat = 4.520855; 
var lng = -74.098308;

function inicio()
{
    var zoom = 6;
    var location = getLocation();

    if(location){
        lat = location[0];
        lng = location[1];
        zoom = 16;
    }
    latlng = new google.maps.LatLng(lat,lng);

    var mapOptions = {
        center: latlng,
        zoom: zoom,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    mapa = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
    if (location) { setMarker(latlng) }
    setAutoComplete();
}

function getLocation()
{
    var geolocation = $("#id_geolocation").val();
    if (geolocation) {
        return geolocation.split(',');
    }
}

function setAutoComplete()
{
    var options = {
        types: ['(cities)','(regions)'],
        componentRestrictions: {country: 'co'}
    };

    var input = document.getElementById('id_address');
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

        latlng = place.geometry.location; 
        setMarker();
        updateLocation(latlng);
    }

function setMarker()
{
    if (marker) {
        updateMarker(latlng);
    } else {
        addMarker();
    }
}

function addMarker()
{
    marker = new google.maps.Marker({
        map: mapa,
        position: latlng,
        draggable:true
    });
    google.maps.event.addListener(marker, 'dragend', alMarkerDrag )
}

    function alMarkerDrag(event)
    {
        updateLocation(event.latLng);
    }

function updateMarker(latlng)
{
    marker.setPosition(latlng);
}

function updateLocation(latlng)
{
    $("#id_geolocation").val(latlng.lat() + "," + latlng.lng());
    mapa.panTo(latlng);
}