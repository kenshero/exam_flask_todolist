from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from TodoModel import Todo

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


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


@app.route('/edit_todo/<int:todo_id>', methods=["PUT"])
def edit_todo(todo_id):
    # import ipdb; ipdb.set_trace();
    # todo = Todo()
    # todo_name = request.form.get('todo_edit_name')
    # user = User.query.get(id)
    # username = request.json['username']
    # email = request.json['email']

    # todo = Todo()
    # todos_data = todo.get_todos()
    return "edit it"


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



# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d' % post_id