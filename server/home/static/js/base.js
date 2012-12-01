function newEventCreated(json)
{
    var event_id = JSON.parse( json )[ "id" ];
    map.addEvent( event_id, parseFloat( $("#inputLatitude").val() ), parseFloat( $("#inputLongitude").val() ) );
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
    var id = $("#currentEvent").attr("event_id");
    map.removeEvent( id );
    $("#currentEvent").hide();
}

$(document).ready( function() {
    $("#removeEventButton").click( removeEvent ); 
    $("#newEventButton").click( newEvent ); 
    map = new Map();
    rescuers = new Rescuers( map );
});
