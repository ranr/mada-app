function Rescuers( map )
{
    this._map = map;
    this._timer = setInterval( $.proxy( this._updateRescuers, this ), 1000 );

    this._updateRescuers = function()
    {
        $.ajax( { url: "/get_all_rescuers",
                    success: $.proxy( this._onRescuersUpdated, this ) } );
    }

    this._onRescuersUpdated = function( json )
    {
    alert("ok");
    }
}
