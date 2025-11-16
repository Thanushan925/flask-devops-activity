# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")


# --- Add a blank line above this to fix E302 ---
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)
