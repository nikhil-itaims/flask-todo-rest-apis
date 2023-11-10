# Register the API routes
from app.api.todos.v1.routes import todo

def get_routes(api):
    """
    Include all the routes from different routes file.
    """
    todo.initialize_urls(api)