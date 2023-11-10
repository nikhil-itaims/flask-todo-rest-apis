from enum import Enum

class BaseAttributes(Enum):
    @classmethod
    def fetch_dict(cls):
        data_dict = {i.name: i.value for i in cls}
        return data_dict

    @classmethod
    def fetch_by_name(cls, name):
        return cls[name].value

    @classmethod
    def fetch_by_id(cls, id):
        data = [i.name for i in cls if i.value == id]
        if data:
            return data[0]
        return None

