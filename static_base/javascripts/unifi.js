$(document).ready( function() {

    $( ".float_menu").hide();

    $(".tag").on( 'click', function( event ) {
        window.location.href = "/tag/" + $(this).attr("pk");
    });

    $( ".group").on( 'mouseenter', function( event ) {
        $( "div.float_menu[pk=\"" + $(this).attr("pk") + "\"]").fadeIn();
    });

    $( ".group").on( 'mouseleave', function( event ) {
        $( "div.float_menu[pk=\"" + $(this).attr("pk") + "\"]").fadeOut();
    });

    $(".wish .control#delete").on( 'click', function( event ) {

        var pk = $(this).attr( "pk" );
        // saving the parent container element in the right scope
        var container = $("div.wish[pk=\"" + pk + "\"]");

        $.ajax({
            type: "DELETE",
            url: "/student/wish/" + pk,
            success: function() {
                container.fadeOut();
            },
            error: function() {
                container.css( "border-color", "red" );
            }
        });
    });


    $(".group .control#leave").on( 'click', function( event ) {

        // this allows a member to leave the group
        // the member is the user in the request

        var pk = $(this).parentNode.attr( "pk" );
        var container = $("div.group[pk=\"" + pk + "\"]");

        $.ajax({
            type: "DELETE",
            url: "/group/" + pk + "/member/",
            success: function() {
                container.fadeOut();
            },
            error: function() {
                container.css( "border-color", "red" );
            }
        });
    });


});