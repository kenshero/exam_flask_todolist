from flask import Flask, jsonify, request
import json

from TodoModel import Todo


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/get_todos')
def get_todos():
    todo = Todo()
    todos_data = todo.get_todos()
    print("todos_data:", todos_data)
    return jsonify(todos_data)


@app.route('/save', methods=["POST"])
def save_todo():
    todo = Todo()
    todo_name = request.form.get('todo_name')
    todo.save_todo(todo_name)
    # todo = Todo()
    # Todo.save_todo()
    return "save it"


@app.route('/edit_todo')
def edit_todo():
    todo = Todo()
    todos_data = todo.get_todos()
    return jsonify(todos_data)


@app.route('/delete_todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo()
    todo.delete_todo(todo_id)
    return "delete it"


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d' % post_id