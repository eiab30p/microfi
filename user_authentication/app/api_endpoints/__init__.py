"""This contains all of the the API routes."""

# If I want to see all API used it is a shorter import
from app.api_endpoints.accounts import LoginUser, ValidateToken
from app.api_endpoints.roles import AddingRoles
from app.api_endpoints.spotify import Callback_auth
from app.api_endpoints.user_routes import UserResource, UserList
