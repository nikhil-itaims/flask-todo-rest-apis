""" It has a todo's CRUD functionality.
"""
from app.constants import constant, status
from app.helpers.standard_response import Response
from app.helpers import helper
from app.messages import validation
from app.messages.todo import ErrorMessage, InfoMessage
from app.api.core.db_method import BaseMethod
from app.api.todos.v1.models.todo import Todo
from app.api.todos.v1.schemas.todo import CreateSchema
from app.api.todos.v1.models.traits.methods.todo \
    import TodoMethod
from app.api.todos.v1.models.traits.attributes.todo \
    import OrderByColumn


class BaseService:
    def __init__(self):
        pass

class TodoService(BaseService):
    def __init__(self):
        pass

    def get_all_todos(self, data: dict):
        """This is used to get all the todos from the database.
        """
        try:
            per_page = data['per_page']
            page = data['page']
            order_op = data['order_op']
            order_by_column = data['order_by_column']
            search_by = data['search_by']
            filter_by = data['filter_by']
            
            column_name=OrderByColumn.fetch_by_id(order_by_column)
            if not column_name:
                order_by_column = constant.ORDER_COLUMN
            else:
                order_by_column = column_name

            todo_obj = TodoMethod()
            
            todos_list, count = todo_obj.fetch_list(order_op, order_by_column, search_by, 
                                    filter_by, page, per_page)
            
            if not todos_list or count==0:
                resp_data = {
                                "todos": [],
                                "count" : constant.STATUS_ZERO
                            }
                response = Response(constant.STATUS_SUCCESS,
                                    resp_data,
                                    ErrorMessage.not_exist_todo).make, \
                                    status.HTTP_200_OK
            
            else:
                todos = CreateSchema().dump(todos_list, many=True)
                
                resp_data = {
                                "count" : count,
                                "todos": todos
                            } 
                response = Response(constant.STATUS_SUCCESS,
                                        resp_data,
                                        InfoMessage.get_todo).make, \
                                        status.HTTP_200_OK
                
        except:
            response = Response(constant.STATUS_ERROR,
                                constant.STATUS_NULL,
                                validation.ErrorMessage.generic_error).make, \
                                status.HTTP_400_BAD_REQUEST  

        return response

    def create_todo(self, data: dict):
        """This function is used to create the todo.

        Args:
            data (dict): It has the status code and message.
        """
        try:
            # Formate the name of todo
            todo_baseobj = BaseMethod(Todo)
            todo_name = helper.stip_string(data['todo_name'])
            to_create_todo = Todo(todo_name)
            # Store the data into the database
            todo_save_obj = BaseMethod(Todo)
            commit_status, todo_obj = todo_save_obj.save(to_create_todo)
            
            if commit_status:
                todo_obj = todo_baseobj.find_by_id(todo_obj.id)
                todo = CreateSchema().dump(todo_obj)

                # Covert the data into json format
                response = Response(constant.STATUS_SUCCESS,
                                    todo,
                                    InfoMessage.create_todo).make, \
                                    status.HTTP_201_CREATED
            else:
                response = Response(constant.STATUS_ERROR,
                                    constant.STATUS_NULL,
                                    validation.ErrorMessage.database_error).make, \
                                    status.HTTP_500_INTERNAL_SERVER_ERROR
            
        except:
            response = Response(constant.STATUS_ERROR,
                                constant.STATUS_NULL,
                                validation.ErrorMessage.generic_error).make, \
                                status.HTTP_400_BAD_REQUEST  

        return response
    
    def get_todo(self, data: dict):
        """This is used to get todo based on Id from the database.
        """
        try:
            todo_baseobj = BaseMethod(Todo)
            
            # Get todo from database.
            todo_obj = todo_baseobj.find_by_id(data['id'])
            todo = CreateSchema().dump(todo_obj)
            
            if not todo:
                response = Response(constant.STATUS_ERROR,
                            constant.STATUS_NULL,
                            ErrorMessage.not_exist_todo).make, \
                            status.HTTP_404_NOT_FOUND
                return response
            else:
                response = Response(constant.STATUS_SUCCESS,
                                    todo,
                                    InfoMessage.get_todo).make, \
                                    status.HTTP_200_OK
            
        except:
            response = Response(constant.STATUS_ERROR,
                                constant.STATUS_NULL,
                                validation.ErrorMessage.generic_error).make, \
                                status.HTTP_400_BAD_REQUEST  
        return response


    def update_todo(self, data: dict): 
        """This function is used to update the todo detail.

        Args:
            data (dict): It has the todo's data.
        """
        try:
            # Check id exist or not
            todo_baseobj = BaseMethod(Todo)
            todo = todo_baseobj.find_by_id(data['id'])
            if not todo:
                response = Response(constant.STATUS_ERROR,
                                        constant.STATUS_NULL,
                                        ErrorMessage.not_exist_todo).make, \
                                        status.HTTP_404_NOT_FOUND
            
            else:
                # Update the todo
                todo.todo_name = data['todo_name']
                todo.updated_at = helper.get_current_datetime()

                commit_status = todo_baseobj.save(todo)
                if commit_status:
                    todo = CreateSchema().dump(todo)
                    response = Response(constant.STATUS_SUCCESS,
                                        todo,
                                        InfoMessage.update_todo).make, \
                                        status.HTTP_200_OK
                else:
                    response = Response(constant.STATUS_ERROR,
                                        constant.STATUS_NULL,
                                        validation.ErrorMessage.database_error).make, \
                                        status.HTTP_500_INTERNAL_SERVER_ERROR
                    

        except:
            response = Response(constant.STATUS_ERROR,
                                constant.STATUS_NULL,
                                validation.ErrorMessage.generic_error).make, \
                                status.HTTP_400_BAD_REQUEST  

        return response
    
    
    def partial_update_todo(self, data: dict): 
        """This function is used to partially update the todo.
            Update the active status of todo.

        Args:
            data (dict): It has the todo's data.
        """
        try:
            # Check id (todo to be update) exist or not
            todo_baseobj = BaseMethod(Todo)
            todo_obj = TodoMethod()
            
            todo = todo_obj.find_by_id(data['id']) 
            if not todo:
                response = Response(constant.STATUS_ERROR,
                                    constant.STATUS_NULL,
                                    ErrorMessage.not_exist_todo).make, \
                                    status.HTTP_404_NOT_FOUND
            else:
                # Update todo
                todo.updated_at = helper.get_current_datetime()

                commit_status = todo_baseobj.save(todo)
                if commit_status:
                    # Covert the data into json format
                    resp_data = CreateSchema().dump(todo)
                    response = Response(constant.STATUS_SUCCESS,
                                        resp_data,
                                        InfoMessage.update_todo).make, \
                                        status.HTTP_200_OK
                else:
                    response = Response(constant.STATUS_ERROR,
                                        constant.STATUS_NULL,
                                        validation.ErrorMessage.database_error).make, \
                                        status.HTTP_500_INTERNAL_SERVER_ERROR
        except:
            response = Response(constant.STATUS_ERROR,
                                constant.STATUS_NULL,
                                validation.ErrorMessage.generic_error).make, \
                                status.HTTP_400_BAD_REQUEST  

        return response
    
    
    def delete_todo(self, data):
        try:
            # Check id (todo to be delete) exist or not
            todo_baseobj = BaseMethod(Todo)
            todo = todo_baseobj.find_by_id(data['id'])
            id = todo.id
            if not todo:
                response = Response(constant.STATUS_ERROR,
                                        constant.STATUS_NULL,
                                        ErrorMessage.not_exist_todo).make, \
                                        status.HTTP_404_NOT_FOUND
            
            else:
                commit_status = todo_baseobj.delete(todo)
                
                if commit_status:
                    resp_data = {"id": id}
                    response = Response(constant.STATUS_SUCCESS,
                                        resp_data,
                                        InfoMessage.delete_todo).make, \
                                        status.HTTP_200_OK
                else:
                    response = Response(constant.STATUS_ERROR,
                                        constant.STATUS_NULL,
                                        validation.ErrorMessage.database_error).make, \
                                        status.HTTP_500_INTERNAL_SERVER_ERROR
        except:
            response = Response(constant.STATUS_ERROR,
                                constant.STATUS_NULL,
                                validation.ErrorMessage.generic_error).make, \
                                status.HTTP_400_BAD_REQUEST  

        return response