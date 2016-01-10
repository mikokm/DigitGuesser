'use strict';

var app = {};

function createQuery(id) {
    var a = $("<a/>",
        {href: "/task/" + id, text: id}
    );

    $("#taskId").append($("<div/>").append(a));
}

function send() {
    var data = {x: $("#inputX").val(), y: $("#inputY").val()};
    console.log(data);

    $.ajax({
        url: "/add",
        type: "POST",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8"
    }).done(function (data) {
        createQuery(data);
    });
}

$(document).ready(function () {
    var canvas = $("#canvas");

    canvas.contextmenu(function (event) {
        event.preventDefault();
        return false;
    });

    app.canvas = new Canvas(canvas[0], 10);
    app.canvas.initialize();
});