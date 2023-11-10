class Response:
    """This class is universal to return standard API responses

    Attributes:
        status (int): The http status response from API
        data (dict/list): The Data from API
        message (str): The message from the API
    """
    def __init__(self, status: int, data: dict, message: str) -> None:
        """This function defines arguments that are used in the class

        Arguments:
            status (int): The http status response from API
            data (dict/list): The Data from API
            message (str): The message from the API

        Returns:
            Returns the API standard response
        """
        self.status = status
        self.data = data
        self.message = message

    @property
    def make(self) -> dict:
        result = {
            'status': self.status,
            'message': self.message,
            'data': self.data
        }

        return result
