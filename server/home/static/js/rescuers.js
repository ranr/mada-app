globalRescuers = null;

function Rescuers( map )
{
    globalRescuers = this;
    this._map = map;
    this._rescuers = [];

    this._updateRescuers = function()
    {
        $.ajax( { url: "/all_rescuers",
                    success: $.proxy( this._onRescuersUpdated, globalRescuers ) } );
    }

    this._onRescuersUpdated = function( json )
    {
        var rescuers = JSON.parse( json );
        for ( i in rescuers ) {
            var id = rescuers[ "phone_number" ];
            if ( this._rescuers[ id ] === undefined )
                this._rescuers[ id ] = new Rescuer( this._map );
            this._rescuers[ id ].update( rescuers[ i ] )
         }
    }

    this._timer = setInterval( $.proxy( this._updateRescuers, this ), 1000 );
}
