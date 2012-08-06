$( function() {
    $(".wish .delete").on( 'click', function( event ) {

        var pk = $(this).attr( "pk" )
        console.info( pk );

        $.ajax({
            type: "DELETE",
            url: "/student/wish/" + pk,
            success: function() {
                $(this).attr({ "type": "hidden" });
            }
        });
    });
});