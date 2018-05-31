"""This contains all of the models for the API."""

# we don't expect Base to be used externally ever
#  from models.base import Role, roles_users
#  from models.user import User
from app.models.user import User
from app.models.role import Role, roles_users
