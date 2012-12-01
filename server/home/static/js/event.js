function Event( map, id, latitude, longitude )
{
    this._map = map;
    this._latitude = latitude;
    this._longitude = longitude;
    this._id = id;

    this._onClick = function()
    {
        $("#currentEvent").find(".latitude").text( this._latitude );
        $("#currentEvent").find(".longitude").text( this._longitude );
        $("#currentEvent").attr("event_id", this._id);
        $("#currentEvent").show();
    }

    this.destroy = function()
    {
        this._marker.setMap( null );
    }

    this._marker = this._map.addMarker( "event", this._latitude, this._longitude );
    google.maps.event.addListener( this._marker, 'click', $.proxy( this._onClick, this ) );
}
