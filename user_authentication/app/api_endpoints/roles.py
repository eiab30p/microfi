# -*- coding: utf-8 -*-
"""
Routes.

This is our basic authentication and other access and permissions.
"""
from flask_restful import Resource, reqparse
from app import api


from app.controllers.user_base_function import addingroles

class AddingRoles(Resource):
    """Testing."""

    parser = reqparse.RequestParser()
    parser.add_argument('roles_list', type=dict,
                        location='json', action='appen')

    def post(self):
        """Docstring."""
        args = self.parser.parse_args(strict=True)
        data = args['roles_list']
        return addingroles(data)


api.add_resource(AddingRoles, '/roles/addroles')
