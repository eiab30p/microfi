"""Actors tables."""

from app import db
from app.models.base import Base

actors_movies = db.Table('actors_movies',
                         db.Column('movie_id', db.Integer(),
                                   db.ForeignKey('movie_catalog.id')),
                         db.Column('actor_id', db.Integer(),
                                   db.ForeignKey('actors.id')))


class Actor(Base):
    """Docstring."""

    __tablename__ = 'actors'
    first_name = db.Column(db.String(255), nullable=False)
    middle_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    def __init__(self, **kwargs):
        """Docstring."""
        super(Actor, self).__init__(**kwargs)

    def __repr__(self):
        """Docstring."""
        return '<Actor %r, %r>' % self.first_name, self.last_name
