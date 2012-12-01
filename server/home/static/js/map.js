function Map()
{
    this._map = null;
    this._events = [];

    this._initalize = function()
    {
        var mapOptions = {
              center: new google.maps.LatLng(32.066158,34.777819),
              zoom: 13,
              mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        this._map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
        this._input = document.getElementById('searchTextField');
        this._autoComplete = new google.maps.places.Autocomplete(this._input);
        this._autoComplete.bindTo('bounds', this._map);
        google.maps.event.addListener(this._autoComplete, 'place_changed', $.proxy( this._placeChanged, this ) );
    }

    this._placeChanged = function()
    {
        var place = this._autoComplete.getPlace();
        if ( ! place.geometry )
            return;
        $("#inputLatitude").val( place.geometry.location.lat() );
        $("#inputLongitude").val( place.geometry.location.lng() );
    }

    this.addEvent = function( id, latitude, longitude )
    {
        this._events[id] = new Event( this, id, latitude, longitude );
    }

    this.removeEvent = function( id )
    {
        this._events[ id ].destroy();
        // todo: remove event
    }

    this.addMarker = function( title, latitude, longitude )
    {
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng( latitude, longitude ),
            map: this._map,
            title:title,
            icon: "/static/images/incident.jpg",
            animation: google.maps.Animation.DROP
        });
        return marker;
    }

    this.addRescuer = function( title, latitude, longitude )
    {
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng( latitude, longitude ),
            map: this._map,
            icon: "/static/images/firstaid.png",
            title:title,
        });
        return marker;
    }

    this._onAllEventsUpdated = function( json )
    {
        var events = JSON.parse( json )[ "events" ];
        for ( i in events )
            this.addEvent( events[ i ]['id'], events[ i ][ 'latitude' ], events[ i ][ 'longitude' ] );
    }

    this._updateAllEvents = function()
    {
        $.ajax( {   url: "/all_events",
                    success: $.proxy( this._onAllEventsUpdated, this ) } );
    }

    this._initalize();
    this._updateAllEvents();
}
