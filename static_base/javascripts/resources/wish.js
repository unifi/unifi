function Wish( pk ) {
    this.delete = function( success, error ) {
        this.request( "delete", {}, success, error );
    };

    this.request = function( method, data, success, error ) {
        var target = [ '/', 'person', '/', 'wish', '/' , pk ].join('');
        var response = $.ajax( {
            type: method, url: target, data: data, success: success, error: error
        } );
    }

}