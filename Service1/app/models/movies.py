"""Docstring."""

from app import db
from app.models.base import Base
from app.models.genre import genres_movies
from app.models.directors import director_movies
from app.models.actors import actors_movies


class Movies(Base):
    """Docstring."""

    __tablename__ = 'movie_catalog'

    title = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(3072), nullable=False)
    year = db.Column(db.String(255), nullable=False)
    runtime = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.String(255))
    votes = db.Column(db.Integer)
    revenue = db.Column((db.Numeric(precision=8, asdecimal=False,
                                    decimal_return_scale=None)))
    genre = db.relationship('Genre', secondary=genres_movies,
                            backref=db.backref('movies', lazy='dynamic'))
    director = db.relationship('Director', secondary=director_movies,
                               backref=db.backref('movies', lazy='dynamic'))
    actors = db.relationship('Actors', secondary=actors_movies,
                             backref=db.backref('movies', lazy='dynamic'))

    def __repr__(self):
        """Docstring."""
        return '<Movies %r>' % self.title
