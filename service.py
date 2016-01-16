from flask import Flask, request, abort
from celery_app import guess
import json

app = Flask("DigitGuesser", static_url_path='/static')


@app.route('/', methods=['GET'])
def root():
    return app.send_static_file("index.html")


@app.route('/guess', methods=['POST'])
def process_hello():
    content = json.loads(request.get_json())
    arr = content['canvas']

    if not content:
        abort(400)
        return

    task = guess.delay(arr)
    return task.id


@app.route('/task/<uuid>')
def task_status(uuid):
    result = guess.AsyncResult(uuid)

    if result.ready():
        return str(result.result)

    return result.state

if __name__ == "__main__":
    app.run(debug=True)
