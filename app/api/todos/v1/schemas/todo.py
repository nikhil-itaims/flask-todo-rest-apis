from marshmallow import fields, Schema
from app.constants import constant
from app.api.core.schema_validation import must_not_be_blank

class GetSchema(Schema):
    """This schema is used to listing the todos.
    """
    per_page = fields.Int(load_default=constant.STATUS_NULL)
    page = fields.Int(load_default=constant.STATUS_NULL)
    order_op = fields.String(load_default=constant.ORDER_OP)
    order_by_column = fields.Int(load_default=constant.ORDER_COLUMN)
    search_by = fields.Str(load_default=constant.STATUS_NULL)
    filter_by = fields.Int(load_default=constant.STATUS_ZERO)

class CreateSchema(Schema):
    """
    This is the Schema for create the todo to validate 
    the fields..
    """
    id= fields.Int(dump_only=True)
    todo_name = fields.Str(required=True, validate=must_not_be_blank)

class PartialUpadteSchema(Schema):
    """
    This is the schema for partially update the todo to validate 
    the fields.
    """
    todo_name = fields.Str(required=True)
