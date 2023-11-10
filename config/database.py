import os
from typing import List, Type
from app.constants import constant
from dotenv import load_dotenv

# It will load the environment variables from the file
load_dotenv()

basedir = os.path.abspath(os.curdir)


class BaseConfig:
    """ Base config of database config
    """
    pass


# MySQL database connection
class MysqlConfig(BaseConfig):
    """ Configurations for the MySQL database connection
    """
    DRIVERNAME = 'mysql'
    HOST = os.getenv('DB_HOST', 'localhost')
    USERNAME = os.getenv('DB_USERNAME')
    PASSWORD = os.getenv('DB_PASSWORD')
    DATABASE = os.getenv('DB_NAME')
    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'connect_timeout': 5
        }
    }
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'


class SqliteConfig(BaseConfig):
    """ Configurations for the sqlite database connection
    """
    DRIVERNAME = 'sqlite'
    USE_MOCK_EQUIVALENCY = constant.STATUS_FALSE
    SECRET_KEY = os.getenv(
        "DATABASE_SECRET_KEY",
        "Rome wasn't build in a day."
        )
    DEBUG = constant.STATUS_TRUE
    SQLALCHEMY_TRACK_MODIFICATIONS = constant.STATUS_FALSE
    TESTING = constant.STATUS_FALSE
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/app.db".format(basedir)


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    MysqlConfig,
    SqliteConfig
]
config_by_name = {cfg.DRIVERNAME: cfg for cfg in EXPORT_CONFIGS}
