function Wish( pk ) {
    this.delete = function( parameters ) {
        this.request( "delete", {}, parameters.success, parameters.error );
    };

    this.request = function( method, data, success, error ) {
        var target = [ '/', 'person', '/', 'wish', '/' , pk ].join('');
        var response = $.ajax( {
            type: method, url: target, data: data, success: success, error: error
        } );
    }
}