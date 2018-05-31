# -*- coding: utf-8 -*-
"""
Routes.

This is our basic authentication and other access and permissions.
"""
from flask import jsonify, make_response, render_template, redirect
from flask_restful import Resource, reqparse, abort
from app import api, app
from datetime import datetime, timedelta
from app.decorators.validation_token import valid_token
import json


# Resource representing a single user
class Route1(Resource):
    """Docstring."""

    @valid_token({'user', 'superadmin'})
    def get(self):
        """Docstring."""
        return json.dumps({'message': 'Testing Get in Route1 service1'})


# Resource representing a list of users
class Route2(Resource):
    """Docstring."""

    def get(self):
        """Docstring."""
        return json.dumps({'message': 'Testing Get in Route2 service1'})


# Endpoints
api.add_resource(Route1, '/1')
api.add_resource(Route2, '/2')
