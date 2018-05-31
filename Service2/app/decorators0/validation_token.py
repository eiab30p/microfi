"""Docstring."""
from functools import wraps
from flask import request, redirect, abort
from app import app
import jwt


def valid_token(users):
    """Docstring."""
    def decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            if request.cookies.get('auth_token') is None:
                return redirect('http://127.0.0.1:5002/login')
            else:
                try:
                    payload = jwt.decode(request.cookies.get('auth_token'),
                                         app.config.get('SECRET_KEY'),
                                         algorithms=['HS256'])
                except jwt.ExpiredSignatureError:
                    return redirect('http://127.0.0.1:5002/login')
                if payload['role']in users:
                    pass
                else:
                    abort(403)
            return f(*args, **kwargs)
        return decorator_function
    return decorator
