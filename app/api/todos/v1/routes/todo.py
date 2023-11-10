"""
Register the routes of todo APIs
"""
from app.api.todos.v1.views import todo

def initialize_urls(api):
    """
    Create the enpoints for the Rest APIs.
    """
    prefix = '/todo'
    api.add_resource(todo.Todo, prefix, endpoint="add_get_todo")
    api.add_resource(todo.TodoDetails, prefix+'/<int:id>', endpoint="update_list_todo")
