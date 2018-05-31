"""Role tables."""

from app import db
from app.models.base import Base
from flask_security import RoleMixin


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('auth_user.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('auth_role.id')))


class Role(Base, RoleMixin):
    """Docstring."""

    __tablename__ = 'auth_role'
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))

    def __init__(self, **kwargs):
        """Docstring."""
        super(Role, self).__init__(**kwargs)

    def __repr__(self):
        """Docstring."""
        return '<Role %r>' % self.name
