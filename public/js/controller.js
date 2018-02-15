angular.module('todoList', ['todoList.service'])
  .controller('todoListController', ['Todo',function(todos) {
    var todoList = this;
    todoList.activeModal = false
    todoList.editTodoData = {}
    todoList.loading = true

    todos.fetchTodoList(function(data){
      todoList.todos = data.data
      console.log(todoList.todos)
      todoList.loading = false
    });

    todoList.saveTodo = (todoName) => {
      var payload = {
        todoName: todoName
      }
      todos.saveTodoList(payload, function(data){
        todos.fetchTodoList(function(data){
          todoList.todos = data.data
          todoList.todoName = ""
        });
      });
    }

    todoList.deleteTodo = (todoID) => {
      todos.deleteTodoList(todoID, function(data){
        todos.fetchTodoList(function(data){
          todoList.todos = data.data
        });
      });
    }

    todoList.editTodo = (todo) => {
      console.log("todo:", todo);
      todoList.activeModal = true
      todoList.editTodoData = {
          todoName: todo[0],
          todoID: todo[1]
      }
    }

    todoList.updateTodo = (editData) => {
      todos.updateTodoList(editData, function(data){
        todos.fetchTodoList(function(data){
          todoList.todos = data.data
          todoList.editTodoData = {}
          todoList.activeModal = false
        });
      });
    }

    todoList.hideModal = () => {
      todoList.activeModal = false
    }

}]);