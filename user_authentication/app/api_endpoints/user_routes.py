"""
User Routes and some Functions.

This is going to be for adding and removing user like funtionsself.
"""
from flask_restful import Resource, reqparse, abort
from app import api
from app.models import User
from app.controllers.user_base_function import list_of_users, create_new_user


# Resource representing a single user
class UserResource(Resource):
    """Docstring."""

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str)
    parser.add_argument('password', type=str)
    parser.add_argument('email', type=str)

    def post(self):
        """Create a new user."""
        args = self.parser.parse_args(strict=True)
        try:
            user = create_new_user(args['username'], args['password'],
                                   args['email'])
            return user, 201
        except IOError:
            abort(400, message="There was an issue adding user")

    def get(self, user_id):
        """Return information about a single user."""
        user = User.query.get(user_id)
        if not user:
            abort(400, message="This user does not exist.")
        return user.to_json, 200


# Resource representing a list of users
class UserList(Resource):
    """Docstring."""

    def get(self):
        """Return a list of users."""
        users = list_of_users()
        if not users:
            abort(400, message="There are no Users, Add a User")
        return users, 200


# Endpoints
api.add_resource(UserResource, '/account', '/<int:user_id>')
api.add_resource(UserList, '/list')
