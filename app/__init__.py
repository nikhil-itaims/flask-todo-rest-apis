"""
The function of this file is to tell the Python interpreter that
this directory is a package and involvement of this __init.py_ file in
it makes it a python project.
"""
import os
from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.constants import constant
from flask_cors import CORS
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow() 

def create_app(env=None):
    from config.database import config_by_name
    from config import app_config
    app = Flask(__name__)
    app.config['SECRET_KEY'] = app_config.AppConfig().SECRET_KEY
    app.config['PROPAGATE_EXCEPTIONS'] = True

    CORS(app)

    """
    Create the Blueprint instance for the API versions.
    create instance of blueprint - 
        api_bp = Blueprint('api', __name__)
        api = Api(api_bp)
        
        # Create endpoint of Rest API
        api.add_resource(UserCreate, '/users', endpoint="")
        app.register_blueprint(api_bp, url_prefix = '/api/v1')

    """

    api_bp_v1 = Blueprint('api1', __name__)
    api_v1 = Api(api_bp_v1)

    app.config.from_object(config_by_name[env or "test"])
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    """
    Register the model files to migrate the database.
    """
    from app.api.todos.v1.models import todo

    """
    Register the blueprints which we have created.
    e.g.- 
        app.register_blueprint(api_bp_v1, url_prefix = '/api/v1')
        app.register_blueprint(api_bp_v2, url_prefix = '/api/v2')
    
    """
    from app.api.todos.v1 import routes as todos_routes
    todos_routes.get_routes(api_v1)

    app.register_blueprint(api_bp_v1, url_prefix = constant.URL_PREFIX_VERSION1)
    return app

# It will load the environment variables from the file
load_dotenv()

database_env = os.getenv("DB_DRIVERNAME") or "sqlite"
app = create_app(database_env)
