/* aliases */
Group.members = Group.persons;

var Tag = {
    get: function( pk ) {
        var message = ["Displaying tag", pk].join(" ");
        console.info( message );
    },

    request: function( method, pk, data, success, error ) {
        var target = [ '/', 'tag', '/' , pk ].join('');
        var response = $.ajax( {
            type: method,
            url: target,
            data: data,
            success: success,
            error: error
        } );

    }
};