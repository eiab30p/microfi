"""Directors tables."""

from app import db
from app.models.base import Base

director_movies = db.Table('director_movies',
                           db.Column('movie_id', db.Integer(),
                                     db.ForeignKey('movie_catalog.id')),
                           db.Column('director_id', db.Integer(),
                                     db.ForeignKey('directors.id')))


class Director(Base):
    """Docstring."""

    __tablename__ = 'directors'
    first_name = db.Column(db.String(255), nullable=False)
    middle_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    def __init__(self, **kwargs):
        """Docstring."""
        super(Director, self).__init__(**kwargs)

    def __repr__(self):
        """Docstring."""
        return '<Director %r, %r>' % self.first_name, self.last_name
