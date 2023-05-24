from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/sub', methods=['POST'])
def subtract():
    data = request.get_json()
    if 'x' not in data or 'y' not in data:
        return jsonify({'error': 'Missing parameters.'}), 400
    result = data['x'] - data['y']
    return jsonify({'result': result}), 200

@app.route('/api/mul', methods=['POST'])
def multiply():
    data = request.get_json()
    if 'x' not in data or 'y' not in data:
        return jsonify({'error': 'Missing parameters.'}), 400
    result = data['x'] * data['y']
    return jsonify({'result': result}), 200

@app.route('/api/div', methods=['POST'])
def divide():
    data = request.get_json()
    if 'x' not in data or 'y' not in data:
        return jsonify({'error': 'Missing parameters.'}), 400
    if data['y'] == 0:
        return jsonify({'error': 'Division by zero.'}), 400
    result = data['x'] / data['y']
    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)