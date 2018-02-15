from flask import Flask, jsonify, request
from flask_cors import CORS

from TodoModel import Todo

app = Flask(__name__)
CORS(app)


@app.route('/get_todos')
def get_todos():
    todo = Todo()
    todos_data = todo.get_todos()
    return jsonify(todos_data)


@app.route('/save', methods=["POST"])
def save_todo():
    try:
        todo = Todo()
        todo_name = request.json['todoName']
        todo.save_todo(todo_name)
        return jsonify({
            "data": "saved todo",
            "error": ""
        })
    except Exception as e:
        return jsonify({
            "data": "",
            "error": "cannot save todo: {}".format(e)
        })


@app.route('/edit_todo', methods=["PUT"])
def edit_todo():
    # import ipdb; ipdb.set_trace();
    try:
        todo_id = request.json['todoID']
        todo_name = request.json['todoName']
        todo = Todo()
        todo.edit_todo(todo_id, todo_name)
        return jsonify({
            "data": "edited todo",
            "error": ""
        })
    except Exception as e:
        return jsonify({
            "data": "",
            "error": "cannot edit todo: {}".format(e)
        })


@app.route('/delete_todo/<int:todo_id>', methods=["DELETE"])
def delete_todo(todo_id):
    try:
        todo = Todo()
        todo.delete_todo(todo_id)
        return jsonify({
            "data": "deleted todo",
            "error": ""
        })
    except Exception as e:
        return jsonify({
            "data": "",
            "error": "cannot deleted todo: {}".format(e)
        })

