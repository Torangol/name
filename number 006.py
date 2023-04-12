from flask import Flask, request

app = Flask(__name__)


@app.route('/imt/', methods=['POST'])
def hello_world():
    b = request.json['data']
    k = request.json['k']
    n = request.json['n']

    return {'res': a}

app.run(host='0.0.0.0', port=5000)
