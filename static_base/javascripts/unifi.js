$(document).ready( function() {


    $(".wish .control#delete").on( 'click', function( event ) {

        var pk = $(this).attr( "pk" );
        // saving the parent container element in the right scope
        var container = $("div.wish[pk=\"" + pk + "\"]");

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


    $(".group #leave").on( 'click', function( event ) {

        // this allows a member to leave the group
        // the member is the user in the request

        var pk = $(this).attr( "pk" );
        var container = $("div.group[pk=\"" + pk + "\"]");

        $.ajax({
            type: "DELETE",
            url: "/group/" + pk + "/member/",
            success: function() {
                container.css( "opacity", "0.1" );
            },
            error: function() {
                container.css( "border-color", "red" );
            }
        });
    });

});