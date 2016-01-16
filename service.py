from flask import Flask, request, abort
from celery_app import add
import json

app = Flask("DigitGuesser", static_url_path='/static')


@app.route('/', methods=['GET'])
def root():
    return app.send_static_file("index.html")


@app.route('/add', methods=['POST'])
def process_hello():
    headers, data = request.headers, request.get_data()

    # print headers
    # print data

    content = json.loads(request.get_json())
    print type(content)
    arr = content['canvas']
    print len(arr)

    if not content:
        abort(400)
        return

    abort(400)

    return "None"

    # task = add.delay(x, y)
    # return task.id


@app.route('/task/<uuid>')
def task_status(uuid):
    result = add.AsyncResult(uuid)

    if result.ready():
        return str(result.result)

    return result.state

if __name__ == "__main__":
    app.run(debug=True)
