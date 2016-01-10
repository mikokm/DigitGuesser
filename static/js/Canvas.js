'use strict';

function Canvas(canvas, pixelSize) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.pixelSize = pixelSize;
    this.grid = new Grid(canvas.width / pixelSize, canvas.height / pixelSize);
}

Canvas.prototype.draw = function () {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    var s = this.pixelSize;
    this.ctx.strokeStyle = 'black';
    this.ctx.fillStyle = 'grey';

    for (var x = 0; x < this.grid.width; ++x) {
        for (var y = 0; y < this.grid.height; ++y) {
            this.ctx.strokeRect(x * s, y * s, s, s);

            if (this.grid.get(x, y)) {
                this.ctx.fillRect(x * s, y * s, s, s);
            }
        }
    }
};

Canvas.prototype.getGrid = function() {
    return grid;
};

Canvas.prototype.handleMouse = function () {
    var button = -1;
    var update = this.updateGrid.bind(this);

    $(window).mousedown(function (event) {
        button = event.button;
    });

    $(window).mouseup(function (event) {
        update(event.clientX, event.clientY, button);
        button = -1;
    });

    $(window).mousemove(function () {
        if (button != -1) {
            update(event.clientX, event.clientY, button);
        }
    });
};

Canvas.prototype.initialize = function () {
    this.draw();
    this.handleMouse();
};

Canvas.prototype.updateGrid = function (x, y, type) {
    var relX = x - this.canvas.offsetLeft;
    var relY = y - this.canvas.offsetTop;
    var gridX = parseInt(relX / this.pixelSize);
    var gridY = parseInt(relY / this.pixelSize);

    if (gridX >= this.grid.width || gridY >= this.grid.height || gridY < 0 || gridX < 0) {
        return;
    }

    if (type == 0) {
        this.grid.set(gridX, gridY, 1);
    } else if (type == 2) {
        this.grid.set(gridX, gridY, 0);
    }

    this.draw();
};