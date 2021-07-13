import logging

from flask import Flask, jsonify, make_response, json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def stat():
    # res = jsonify(success=True)
    data = {'result': 'OK - healthy'}
    return make_response(jsonify(data))


@app.route('/stat')
def health_check():
    response = app.response_class(
        response=json.dumps({'result': 'OK - healthy'}), status=200, mimetype='application/json'
    )
    app.logger.info('status ok')
    return response


@app.route('/met')
def mets():
    response = app.response_class(
        response=json.dumps({'status': 'success', 'code': 0, 'data': {"UserCount": 140, 'UserCountActive': 23}}),
        status=200, mimetype='application/json'
    )
    app.logger.info('metrics ok')
    return response


@app.route("/metrics")
def metr():
    data = {"UserCount": 140, 'UserCountActive': 23}
    return make_response(jsonify(data))


if __name__ == "__main__":
    # filename = os.path.join(os.path.dirname(os.path.relpath(__file__)), 'app.log')
    logging.basicConfig(
        filename='app.log',
        level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8080)
