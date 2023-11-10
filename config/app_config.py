import os
from dotenv import load_dotenv

# It will load the environment variables from the file
load_dotenv()


class AppConfig:
    """ App Configurations 
    """
    SECRET_KEY = os.getenv('SECRET_KEY')
    BASE_URL = os.getenv('BASE_URL')