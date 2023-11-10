import time
from marshmallow import ValidationError
from app.messages.validation import ErrorMessage

# Custom validator
def must_not_be_blank(data):
    if data=="" or data==None:
        raise ValidationError(ErrorMessage.not_be_null)
