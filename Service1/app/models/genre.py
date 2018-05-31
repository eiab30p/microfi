"""Directors tables."""

from app import db
from app.models.base import Base

genres_movies = db.Table('genres_movies',
                         db.Column('movie_id', db.Integer(),
                                   db.ForeignKey('movie_catalog.id')),
                         db.Column('genre_id', db.Integer(),
                                   db.ForeignKey('genres.id')))


class Genre(Base):
    """Docstring."""

    __tablename__ = 'genres'
    type = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, **kwargs):
        """Docstring."""
        super(Genre, self).__init__(**kwargs)

    def __repr__(self):
        """Docstring."""
        return '<Genre %r>' % self.type
