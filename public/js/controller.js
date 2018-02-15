angular.module('todoList', ['todoList.service'])
  .controller('todoListController', ['Todo',function(todos) {
    var todoList = this;

    todos.fetchTodoList(function(data){
      todoList.todos = data.data
      console.log(todoList.todos)
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

}]);