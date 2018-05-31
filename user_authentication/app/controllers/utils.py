"""Docstring."""

from flask import g
from app import app, db, user_datastore
from app.models import Role, User
from flask_restful import abort
from sqlalchemy.exc import IntegrityError
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer,
    BadSignature,
    SignatureExpired
)

from flask_security.utils import hash_data, verify_hash


def authenticate(username, password):
    """Docstring."""
    user = User.query.filter_by(username=username).first()
    if user is None:
        return({'status_code': 400, 'message': "User does not exist"})
    if verify_hash(user.password, password):
        g.current_user = user
        return({'status_code': 200, 'data': user})
    return({'status_code': 400, 'message': "There was an Issue logging In"})
