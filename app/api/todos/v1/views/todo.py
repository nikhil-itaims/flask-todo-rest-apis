"""
These views are Python functions that takes http requests and 
returns http response.
"""
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from app.constants import constant, status
from app.helpers.standard_response import Response
from app.messages.validation import ErrorMessage
from app.api.todos.v1.services.todo import TodoService
from app.api.todos.v1.schemas.todo import \
    CreateSchema, GetSchema, PartialUpadteSchema


class Todo(Resource):
    """This API is used to perform the get all and create operation on a brand.
    """
    
    def get(self):
        # Fetch the data from the query params
        req_data = request.args
        
        try:
            data = GetSchema().load(req_data)
        except ValidationError as err:
            if err.messages:
                error_message = list(err.messages.values())[0][0]
            else:
                error_message = ErrorMessage.invalid_req_parameter
            response = Response(constant.STATUS_ERROR,
                                constant.STATUS_NULL,
                                error_message).make
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return response, status_code

        # Call the service to get todos
        response, status_code = TodoService().get_all_todos(data)

        return response, status_code
    
    def post(self):
        # Validate the request data
        req_data = request.get_json()
        
        try:
            data = CreateSchema().load(req_data)
        except ValidationError as err:
            if err.messages:
                error_message = list(err.messages.values())[0][0]
            else:
                error_message = ErrorMessage.invalid_req_parameter
            response = Response(constant.STATUS_ERROR,
                                constant.STATUS_NULL,
                                error_message).make
            status = constant.STATUS_CODE_422
            return response, status

        # Call the service to create the todo.
        response, status = TodoService().create_todo(data)

        return response, status    

class TodoDetails(Resource):
    def get(self, id: int):
        data={}
        data['id']=id
        # Call the service to get the todo detail
        response, status_code = TodoService().get_todo(data)

        return response, status_code 
    
    
    def put(self, id: int):
        # Validate the request data
        req_data = request.get_json()
        
        try:
            data = CreateSchema().load(req_data)
        except ValidationError as err:
            if err.messages:
                error_message = list(err.messages.values())[0][0]
            else:
                error_message = ErrorMessage.invalid_req_parameter
            response = Response(ErrorMessage.status_error,
                                constant.STATUS_NULL,
                                error_message).make
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return response, status_code

        # Call the service to update the brand
        data['id']=id
        response, status_code = TodoService().update_todo(data)

        return response, status_code 
    
    def patch(self, id: int):
        # Validate the request data
        req_data = request.get_json()
        
        try:
            data = PartialUpadteSchema().load(req_data)
        except ValidationError as err:
            if err.messages:
                error_message = list(err.messages.values())[0][0]
            else:
                error_message = ErrorMessage.invalid_req_parameter
            response = Response(ErrorMessage.status_error,
                                constant.STATUS_NULL,
                                error_message).make
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return response, status_code
        
        # Call the service to update the brand
        data['id']=id
        response, status_code = TodoService().partial_update_todo(data)

        return response, status_code

    def delete(self, id: int):
        data={}
        data['id']=id
        response, status_code = TodoService().delete_todo(data)

        return response, status_code