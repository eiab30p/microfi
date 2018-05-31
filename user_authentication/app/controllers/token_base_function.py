"""Docstring."""
from flask import g
from app import app
from app.models import User
from datetime import datetime, timedelta
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer,
    BadSignature,
    SignatureExpired
)
import jwt


def validate_token(token):
    """Docstring."""
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None
    except BadSignature:
        return None
    user = User.query.get(data['id'])
    g.current_user = user
    return user


def generate_token(value, exp_time=15):
    """Docstring."""
    token_data = ','.join(['{}:{}'.format(key,  val)
                          for key, val in value.items()])

    token_with_time = '{},{}:{},{}:{}'.format(token_data, 'exp',
                                              datetime.utcnow() +
                                              timedelta(minutes=exp_time),
                                              'iat', datetime.utcnow()
                                              )
    print(token_with_time)
    token = jwt.encode({token_with_time}, app.config.get('SECRET_KEY'), algorithm='HS256')
    return token


def get_token_value(auth_token):
    """Docstring."""
    values = jwt.decode(auth_token,
                        app.config.get('SECRET_KEY'),
                        algorithms=['HS256'])
    return values
