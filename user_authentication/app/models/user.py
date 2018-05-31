"""
User Database.

backref is a simple way to also declare a new property on the Address class.
You can then also use my_address.person to get to the person at that address.
lazy defines when SQLAlchemy will load the data from the database:

'select' (which is the default) means that SQLAlchemy will load the data as
necessary in one go using a standard select statement.

'joined' tells SQLAlchemy to load the relationship in the same query as the
parent using a JOIN statement.

'subquery' works like 'joined' but instead SQLAlchemy will use a subquery.

'dynamic' is special and useful if you have many items. Instead of loading the
items SQLAlchemy will return another query object which you can further refine
before loading the items. This is usually what you want if you expect more than
a handful of items for this relationship.

src: http://flask-sqlalchemy.pocoo.org/2.1/models/
"""

from app.models.base import Base
from app.models.role import roles_users
from flask_security import UserMixin
from app import db


class User(Base, UserMixin):
    """Docstring."""

    __tablename__ = 'auth_user'
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(45))
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        """Docstring."""
        return '<User %r>' % self.email
