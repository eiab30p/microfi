# -*- coding: utf-8 -*-
"""
Routes.

This is our basic authentication and other access and permissions.
"""
from flask import make_response, render_template, redirect, request
from flask_restful import Resource
from app import api, app
from app.decorators.validation_token import valid_token
import json
import requests
from six.moves.urllib.parse import quote


# Resource representing a single user
class Route1(Resource):
    """Docstring."""

    @valid_token({'user', 'superadmin'})
    def get(self):
        """Docstring."""
        return json.dumps({'message': 'Testing Get in Route1 service2'})


class Route3(Resource):
    """Docstring."""

    def get(self, display_arr):
        """Docstring."""
        return make_response(render_template('index.html',
                                             mimetype='text/html',
                                             sorted_array=display_arr))


# Endpoints
api.add_resource(Route1, '/1')
api.add_resource(Route3, '/3')
