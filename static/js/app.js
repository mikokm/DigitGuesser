"use strict";

function send() {
    var data = { x: $("#inputX").val(), y: $("#inputY").val() };
    console.log(data);

    $.ajax({
        url: "/add",
        type: "POST",
        data: JSON.stringify(data),
        contentType: "application/json",
        success: function(data, status) {
            alert(data);
        }
    });
}
