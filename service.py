from flask import Flask, request
from celery_app import add

app = Flask("OCR-service", static_url_path='/static')


@app.route('/', methods=['GET'])
def root():
    return app.send_static_file("index.html")


@app.route('/add', methods=['POST'])
def process_hello():
    # print request.headers
    # print request.get_data()
    content = request.get_json()

    if not content:
        return "Invalid request."

    x = int(content['x'])
    y = int(content['y'])

    print "Executing task with x=%s, y=%s" % (x, y)

    task = add.delay(x, y)
    return task.id


@app.route('/task/<uuid>')
def task_status(uuid):
    result = add.AsyncResult(uuid)

    if result.ready():
        return str(result.result)

    return result.state

if __name__ == "__main__":
    app.run(debug=True)
