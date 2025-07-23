from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/todos', methods=['GET'])
def hello_world():
    # You can convert that variable into a json string like this
    json_text = jsonify(todos)

    # And then you can return it to the front end in the response body like this
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_todo = request.json
    todos.append(request_todo)
    print("Incoming request with the following body", todos)
    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    print("This is the position to delete:", index)
    jsonify_text = jsonify(todos)
    return jsonify_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)