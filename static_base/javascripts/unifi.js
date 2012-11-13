function modelRequest( method, model, pk, payload ) {

    var target = ["/", model, "/", pk].join( "" );
    var result = $.ajax({
        type: method,
        url: target,
        success: function() {

        },
        error: function() {

        }
    });
    return result
}


function refresh() {

    $.ajax({
        type: "GET",
        url: "/my/wish/",
        dataType: "html",
        success: function( data ) {
            $( "#wishes" ).html( data );
        },
        error: function() {}
    });

    $.ajax({
        type: "GET",
        url: "/my/group/",
        dataType: "html",
        success: function( data ) {
            $("#groups").html( data );
            $( ".group .menu").hide();
        },
        error: function() {}
    });

    $.ajax({
        type: "GET",
        url: "/my/assistance/",
        dataType: "html",
        success: function( data ) {
            $("#assistance").html( data )
        },
        error: function() {}
    });

    $.ajax({
        type: "GET",
        url: "/my/assistance/",
        dataType: "html",
        success: function( data ) {
            $("#assistance").html( data )
        },
        error: function() {}
    });
}

function highlight( selector ) {

    var state = {
        'on': 0.9,
        'off': 1.0
    }

    $(document).on( 'mouseover', selector, function( event ) {
        $(this).css( 'opacity', state['on'] );
    });

    $(document).on( 'mouseout', selector, function( event ) {
        $(this).css( 'opacity', state['off'] );
    });
}

$(document).ready( function() {


    highlight( ".person" );
    highlight( ".tag" );

    refresh();

    $( ".group.menu").slideDown();


    $( ".modal#contactPopup" ).modal( {
        show: false,
        backdrop: "static"
    });

    $( ".modal#notification" ).modal( {
        show: false,
        backdrop: "static"
    });

    /*
     *  Initialize Tagit
     */
    $.get(
        url='/tag/distribution/?format=json',
        success=function( distribution ) {
            $( "#tagit_form" ).tagit( {
                availableTags: distribution,
                allowSpaces: true,
                fieldName: "tags",
                itemName: "user",
                tabIndex: 1
            })
        },
        format="json"
    );

    /*
     *  Wish object controls
     */
    $(document).on( 'click', ".wish .actions button#delete", function( event ) {
        var pk = $(this).attr( "pk" );
        // saving the parent container element in the right scope
        var container = $("div.wish[pk=\"" + pk + "\"]");

        $.ajax({
            type: "DELETE",
            url: "/person/wish/" + pk,
            success: function() {
                container.fadeOut(1000);
                refresh();
            },
            error: function() {
                container.css( "border-color", "red" );
            }
        });
    });








    // this allows a member to leave the group
    // the member is the user in the request
    $(document).on( 'click', ".group .menu button#leave", function( event ) {
        var pk = $(this).parent().parent().parent().attr( "pk" );
        var container = $("div.group[pk=\"" + pk + "\"]");

        $.ajax({
            type: "DELETE",
            url: "/group/" + pk + "/member/",
            success: function() {
                container.fadeOut(1000);
                refresh();
            },
            error: function() {
                container.css( "border-color", "red" );
            }
        });

    });

    // allows a member to join a group
    $(document).on('click', ".group button#join", function (event) {
        var pk = $(this).parent().parent().parent().parent().attr( "pk" );
        var container = $("div.group[pk=\"" + pk + "\"]");

        $.ajax({
            type:"PUT",
            url:"/group/" + pk + "/member/",
            success:function () {
                $( ".group .menu button#join" ).fadeOut();
                document.location.reload(true)
                refresh();
            }
        });
    });

    $(document).on( 'click', ".group .menu button#assist", function( event ) {
        var pk = $(this).parent().parent().parent().attr( "pk" );
        $.post(
            "/group/" + pk,
            { 'needs_assistance': 1 }
        );
    });


    $(document).on( 'mouseenter', ".group", function( event ) {
        $( "div.menu[pk=\"" + $(this).attr("pk") + "\"]").slideDown();
    });

    $(document).on( 'mouseleave', ".group", function( event ) {
        $( "div.menu[pk=\"" + $(this).attr("pk") + "\"]").slideUp();
    });

});