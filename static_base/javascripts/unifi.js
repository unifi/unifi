$(document).ready( function() {

    $( ".menu" ).hide();

    /* tag model */
    /* content view links */
    $(document).on( 'click', ".tag",  function( event ) {
        window.location.href = "/tag/" + $(this).attr("pk");
    });

    /*
        [!] fix the tag on-click, on-mouseover behavior for the elements inside
        the new-wish container: either by applying the handler just to elements
        outside, or by excluding the elements inside of the tagger
    */

    /* highlighting */
    $(document).on( 'mouseover', ".tag", function( event ) {
        $(this).fadeTo( 'slow', 0.75 );
    });

    $(document).on( 'mouseout', ".tag", function( event ) {
        $(this).fadeTo( 'fast', 1 );
    });


    /* student model */
    /* content view links */
    $(document).on( 'click', ".student", function( event ) {
        window.location.href = "/student/" + $(this).attr("pk");
    });

    /* highlighting */
    $(document).on( 'mouseover', ".student", function( event ) {
        $(this).fadeTo( 'slow', 0.75 );
    });

    $(document).on( 'mouseout', ".student", function( event ) {
        $(this).fadeTo( 'fast', 1 );
    });

    $(document).on( 'mouseenter', ".group", function( event ) {
        $( "div.menu[pk=\"" + $(this).attr("pk") + "\"]").fadeIn('fast');
    });

    $(document).on( 'mouseleave', ".group", function( event ) {
        $( "div.menu[pk=\"" + $(this).attr("pk") + "\"]").fadeOut('slow');
    });

    $(document).on( 'click', ".wish .control#delete", function( event ) {

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


    $(document).on( 'click', ".wish .control#delete", function( event ) {

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