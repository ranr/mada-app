function Rescuer( map )
{
    this._map = map;
    this._marker = null;
    this._currentDisplayedLatitude = null;
    this._currentDisplayedLongitude = null;

    this.update = function( data )
    {
        var marker = this._marker;
        this._latitude = parseFloat( data[ 'latitude' ] );
        this._longitude = parseFloat( data[ 'longitude' ] );

        if ( ! this._shouldUpdate() )
            return;

        this._currentDisplayedLatitude = this._latitude;
        this._currentDisplayedLongitude = this._longitude;
        this._marker = this._map.addRescuer( "rescuer", this._latitude, this._longitude );
        if ( marker != null )
            marker.setMap( null );
    }

    this._shouldUpdate = function()
    {
        return ( this._currentDisplayedLatitude != this._latitude   || 
                this._currentDisplayedLongitude != this._longitude ); 
    }
}
