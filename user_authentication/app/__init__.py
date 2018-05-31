"""
Initializing Application.

The script above simply creates the application object (of class Flask).
and then imports the views module, which we haven't written yet. Do not
confuse app the variable (which gets assigned the Flask instance) with
app the package (from which we import the views module).

Other Stuff Gose Here
"""

from flask import Flask
from config import Config
from flask_wtf import CSRFProtect
from flask_mail import Mail
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_security.datastore import SQLAlchemyUserDatastore
from flask_security import Security

# Creating App
app = Flask(__name__)

# get config information
app.config.from_object(Config)

# Creating API
api = Api(app)

# Setting CSRFProtect
csrf = CSRFProtect(app)

# Enabling Email Capabilities
mail = Mail(app)

# Enabling DB connection
db = SQLAlchemy(app, session_options={'autocommit': False, 'autoflush': False})

manager = Manager(app)
migrate = Migrate(app, db)

from app.models import User, Role

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)


# Need to have all the other settings set up before we import APIs
from app.api_endpoints import LoginUser, ValidateToken, AddingRoles,\
                              Callback_auth, UserResource, UserList

security = Security(app, user_datastore, login_form=LoginUser)


# This is HTTP Access Control between sites. * needs to be replaced with
# IP addresses and more secure settings.
@app.after_request
def after_request(response):
    """Docstring."""
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, *')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE')
    return response
