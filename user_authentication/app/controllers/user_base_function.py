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


# Helper functions
def create_new_user(username, password, email, roles='user'):
    """Docstring."""
    if username is None or password is None or email is None:
        abort(400, message="Ensure you Are Passing Valid Arguments.")
    if User.query.filter_by(username=username).first() is not None:
        abort(400, message="User already exist.")
    try:
        user_datastore.create_user(username=username,
                                   password=hash_data(password),
                                   email=email, first_name="testing")
        db.session.commit()
        user_datastore.add_role_to_user(email, roles)
        db.session.commit()
    except Exception as e:
        abort(400, message="There is an issue adding this record")

    return "Testing"


# We building queries so we can call in other places
def addingroles(list_of_roles):
    """Docstring."""
    try:
        user_datastore.find_or_create_role(name=list_of_roles['name'],
                                           description=list_of_roles['description'])
    except Exception:
        db.session.rollback()
        for u in list_of_roles:
            user_datastore.find_or_create_role(name=u['name'],
                                               description=u['description'])
    return 200


def list_of_users():
    """Docstring."""
    users = User.query.all()
    return {"users": [u.email for u in users]}
