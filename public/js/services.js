angular.module('todoList.service', [])
  .factory('Todo', ['$http', function($http) {
    return {
      fetchTodoList: function(callback) {
        $http.get('http://159.65.2.203:5000/get_todos').then(function(response){
          callback(response)
        })
        .catch(function(data, status, headers, config){
          callback({error: data});
        });
      },
      saveTodoList: function(payload, callback) {
        $http.post('http://159.65.2.203:5000/save', payload).then(function(response){
          if(response.error) {
            console.log("Error:", response.error);
          }
          callback(response)
        })
        .catch(function(data, status, headers, config){
          callback({error: data});
        });
      },
      deleteTodoList: function(todoID, callback) {
        $http.delete(`http://159.65.2.203:5000/delete_todo/${todoID}`).then(function(response){
          if(response.error) {
            console.log("Error:", response.error);
          }
          callback(response)
        })
        .catch(function(data, status, headers, config){
          callback({error: data});
        });
      },
      updateTodoList: function(payload, callback) {
        $http.put(`http://159.65.2.203:5000/edit_todo`, payload).then(function(response){
          if(response.error) {
            console.log("Error:", response.error);
          }
          callback(response)
        })
        .catch(function(data, status, headers, config){
          callback({error: data});
        });
      }
    }
  }]);