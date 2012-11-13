

function Group( pk ) {

    this.get = function( parameters ) {
        var message = ["Displaying group", pk].join(" ");
        console.info( message );
    };

    this.join = function( parameters ) {
        var message = [Person.pk, "joins group", pk].join(" ");
        console.info( message );
        this.persons.request( "put", "", {}, parameters.success, parameters.error );
    };

    this.contact = function( parameters ) {
        var message = [Person.pk, "is contacting group", pk].join(" ");
        console.info( message );
    };

    this.leave = function( parameters ) {
        /* remove a member: called by a member */
        var message = ["Member", Person.pk, "attempts to leave group", pk].join(" ");
        console.info( message );
        this.persons.request( "delete", "", {}, parameters.success, parameters.error );
    };

    /* submodels */
    this.assistance = new GroupAssistance(pk);
    this.persons = new GroupPersons(pk);

    /* request */
    this.request = function( method, pk, data, success, error ) {
        var target = [ '/', 'group', '/' , pk ].join('');
        var response = $.ajax( {
            type: method, url: target, data: data, success: success, error: error
        } );
    };
}


function GroupAssistance( pk ) {
    this.on = function() {
        var message = ["Group", pk, "requires assistance by", Person.pk].join(" ");
        console.info( message );
        return this.request( "post", { 'needs_assistance': 1 } )
    };

    this.off = function() {
        var message = ["Group", pk, "does not require assistance by", Person.pk].join(" ");
        console.info( message );
        this.request( "post",
            { 'needs_assistance': 0 } )
    };

    /* request */
    this.request = function( method, data, success, error ) {
        var target = [ '/', 'group', '/' , pk ].join('');
        var response = $.ajax( {
            type: method, url: target, data: data, success: success, error: error
        } );
    }
}

/* persons: a field for members of a group */
function GroupPersons( pk ) {

    this.add = function( personPk ) {
        var message = ["Adding the member", personPk, "to group", pk].join(" ");
        console.info( message );
        this.request( "put", personPk )
    };

    this.delete = function( personPk ) {
        /* remove a member of a group */
        var message = ["Removing member", personPk, "from group", pk].join(" ");
        console.info( message );
        this.request( "delete", pk, personPk );
    };

    this.contains = function( personPk ) {
        var message = ["Checking if", personPk, "is member of", pk].join(" ");
        console.info( message );
    };

    /* request */
    this.request = function( method, personPk, data, success, error ) {
        var target = [ '/', 'group', '/', pk, '/member/', personPk ].join('');
        console.info( "here" );
        var response = $.ajax( {
            type: method, url: target, data: data, success: success, error: error
        } );
    };
}