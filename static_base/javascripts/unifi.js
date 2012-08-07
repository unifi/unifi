$(document).ready( function() {


    $(".wish .delete").on( 'click', function( event ) {

        var pk = $(this).attr( "pk" );
        // saving the parent container element in the right scope
        var container = $("div[pk=\"" + pk + "\"][model=\"Wish\"]");

        $.ajax({
            type: "DELETE",
            url: "/student/wish/" + pk,
            success: function() {
                container.css( "opacity", "0.1" );
            },
            error: function() {
                container.css( "border-color", "red" );
            }
        });
    });

});