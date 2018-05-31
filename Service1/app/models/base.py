"""Based tables."""

from app import db


# A base model for other database tables to inherit
class Base(db.Model):
    """Docstring."""

    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
