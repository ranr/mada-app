function Rescuer( map, data )
{
    this._map = map;
    this._marker = null;

    this.update = function( data )
    {
        this._latitude = parseFloat( data[ 'latitude' ] );
        this._longitude = parseFloat( data[ 'longitude' ] );

        var marker = this._marker;
        this._marker = this._map.addRescuer( "rescuer", this._latitude, this._longitude );
        if ( marker != null )
            marker.setMap( null );
    }
}
