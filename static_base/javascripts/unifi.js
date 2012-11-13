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
        'on': 0.95,
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

    /* enable highlighting on elements */
    highlight( ".person" );
    highlight( ".tag" );

    /* refresh the dynamic views */
    refresh();

    /* hide the menu */
    $( ".group.menu").slideDown();


    $( ".modal#contactPopup" ).modal( {
        show: false,
        backdrop: "static"
    });

    $( ".modal#notification" ).modal( {
        show: false,
        backdrop: "static"
    });

    /* Initialize Tagit */
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

    $(document).on( 'mouseenter', ".group", function( event ) {
        $( "div.hint[pk=\"" + $(this).attr("pk") + "\"]").slideUp();
        $( "div.menu[pk=\"" + $(this).attr("pk") + "\"]").slideDown();
    });

    $(document).on( 'mouseleave', ".group", function( event ) {
        $( "div.hint[pk=\"" + $(this).attr("pk") + "\"]").slideDown();
        $( "div.menu[pk=\"" + $(this).attr("pk") + "\"]").slideUp();
    });


    /*
     *  Wish object controls
     */








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
            type: "PUT",
            url: "/group/" + pk + "/member/",
            success:function () {
                $( ".group .menu button#join" ).fadeOut();
                document.location.reload(true)
                refresh();
            }
        });

    });






    $(document).on( 'click', ".group .menu button#assist", function() {
        var groupPk = $(this).parent().parent().parent().attr("pk");
        var groupInstance = new Group( groupPk );
        groupInstance.assistance.on();
    });

    $(document).on( 'click', ".wish .actions button#delete", function( event ) {
        var pk = $(this).attr( "pk" );
        var wishInstance = new Wish(pk);
        var container = $("div.wish[pk=\"" + pk + "\"]");
        wishInstance.delete(
            function() {
                container.fadeOut(1000);
                refresh();
            },
            function() {
                container.css( "border-color", "red" );
            }
        )
    });


});