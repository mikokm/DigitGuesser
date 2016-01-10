"use strict";

function createQuery(id) {
    var a = $("<a/>",
        { href: "/task/" + id, text: id }
    );

    $("#taskId").append($("<div/>").append(a));
}

function send() {
    var data = { x: $("#inputX").val(), y: $("#inputY").val() };
    console.log(data);

    $.ajax({
        url: "/add",
        type: "POST",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8"
    }).done(function(data) {
        createQuery(data);
    });
}
