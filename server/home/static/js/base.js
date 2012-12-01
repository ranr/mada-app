function newEventCreated()
{
    map.addEvent( parseFloat( $("#inputLatitude").val() ), parseFloat( $("#inputLongitude").val() ) );
}

function newEvent()
{
    $.ajax( {   url: "/new_event/" + $("#inputLatitude").val() + "/" + $("#inputLongitude").val(),
                success: newEventCreated,
                error: function() {} } );
}

function removeEvent()
{
    var currentEvent = $("#currentEvent")
    var latitude = $("#currentEvent.latitude").val();
    var longitude = $("#currentEvent.longitude").val();
    map.removeEvent( latitude, longitude );
    $("#currentEvent").hide();
}

$(document).ready( function() {
    $("#removeEventButton").click( removeEvent ); 
    $("#newEventButton").click( newEvent ); 
    map = new Map();
});
