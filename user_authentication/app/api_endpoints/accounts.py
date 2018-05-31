# -*- coding: utf-8 -*-
"""
Routes.

This is our basic authentication and other access and permissions.
"""
from flask import make_response, render_template, redirect
from flask_restful import Resource, reqparse, abort
from app import api
from app.controllers.utils import authenticate
from app.controllers.token_base_function import generate_token, validate_token
from app.controllers.spotify_controller import generate_spotify_auth_url

# Authenticate a user's username/password, returns a token upon success
class LoginUser(Resource):
    """Docstring."""

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str)
    parser.add_argument('password', type=str)

    def get(self):
        """Docstring."""
        resp = make_response(render_template('landing_page.html',
                                             mimetype='text/html'))
        return resp

    def post(self):
        """Return json web token for a valid user."""
        # Temp hard coded need to get from input
        user = authenticate('everde5', '2brownie5')

        if user['status_code'] == 400:
            return user

        token_data = {'username': user['data'].username,
                      'role': user['data'].roles[0].name}
        token = generate_token(token_data)

        auth_url = generate_spotify_auth_url

        resp = make_response(redirect(auth_url, 302))
        resp.set_cookie('auth_token', token.decode('utf-8'))

        return resp


# Determines if a json web token is valid for a given user account
class ValidateToken(Resource):
    """Docstring."""

    parser = reqparse.RequestParser()
    parser.add_argument('token', type=str)

    def post(self):
        """Docstring."""
        args = self.parser.parse_args(strict=True)
        user = validate_token(args['token'])
        if user is None:
            abort(400, message="User does not exist")
        return {'token': args['token'], 'user': user.to_json}, 200


# Endpoints
api.add_resource(LoginUser, '/login')
api.add_resource(ValidateToken, '/authenticate')
