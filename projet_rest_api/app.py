from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello wtf bitchfffdfes World!")

@app.route('/api/testing', methods=['POST'])
def testing():
    return jsonify(message="jjsjsj")

if __name__ == '__main__':
    app.run(debug=True)