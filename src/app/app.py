from gait import gait_calculation
from flask import Flask, request, jsonify

app = Flask(__name__)

#
@app.route('/', methods=['GET'])
def index():
    return '<h1>hello</h1>'
@app.route('/gaitanalyze', methods=['POST']) 
def gaitanalyze():
    data = request.json
    key = 'selectedValues'
    selectedKeys = data[key]
    del data[key]
    result = gait_calculation(data,selectedKeys)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0')