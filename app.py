from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({'message': 'Hello, Welcome to my Flask app!'})

if __name__ == '__main__':
    app.run(debug=True)
