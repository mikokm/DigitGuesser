'use strict';

var app = {};

function createQuery(id) {
    var a = $("<a/>",
        {href: "/task/" + id, text: id}
    );

    $("#taskId").append($("<div/>").append(a));
}

app.clearCanvas = function () {
    app.canvas.clear();
};

app.sendCanvas = function () {
    var data = app.canvas.toJSON();

    $.ajax({
        url: "/guess",
        type: "POST",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8"
    }).done(function (data) {
        createQuery(data);
    }).fail(function () {
        console.log("Ajax request failed.")
    });
};

$(document).ready(function () {
    var canvas = $("#canvas");

    canvas.contextmenu(function (event) {
        event.preventDefault();
        return false;
    });

    app.canvas = new Canvas(canvas[0], 8);
    app.canvas.initialize();
});