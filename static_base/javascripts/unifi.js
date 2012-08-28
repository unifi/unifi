$(document).ready( function() {

    $( ".menu" ).hide();
    $( ".focus").hide();

    /* tag model */
    /* content view links */
    $(document).on( 'click', ".tag",  function( event ) {

    });

    /*
        the new-wish container: either by applying the handler just to elements
        outside, or by excluding the elements inside of the tagger
    */

    var focusAnimationTime = 200;


    function displayFocusProfile( target ) {
        var model = target.attr( 'model' );
        var pk = target.attr( 'pk' );
        var uri = "/" + model + "/" + pk + "?format=json";

        $.ajax({
            type: "GET",
            url: uri,
            success: function() {},
            error: function() {}
        });
    }

    /* highlighting */
    $(document).on( 'mouseover', ".tags .tag", function( event ) {
        $(this).fadeTo( 'slow', 0.75 );
        /* element info via rest request */
        $(".focus").html( $(this).clone() );
        $(".focus").fadeIn( focusAnimationTime );
    });

    $(document).on( 'mouseout', ".tags .tag", function( event ) {
        $(this).fadeTo( 'fast', 1 );
        /* reset focus state */
        /* $(".focus").html( "" ); */
        $(".focus").fadeOut( focusAnimationTime );
    });


    /* student model */
    /* content view links */

    $(document).on( 'mouseover', ".students .student", function( event ) {
        $(this).fadeTo( 'slow', 0.75 );
        /* element info via rest request */
        $(".focus").html( $(this).clone() );
        $(".focus").fadeIn( focusAnimationTime );
    });

    $(document).on( 'mouseout', ".students .student", function( event ) {
        $(this).fadeTo( 'fast', 1 );
        /* reset focus state */
        /* $(".focus").html( "" ); */
        $(".focus").fadeOut( focusAnimationTime );
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