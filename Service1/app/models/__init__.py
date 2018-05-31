"""This contains all of the models for the API."""

# we don't expect Base to be used externally ever
#  from models.base import Role, roles_users
#  from models.user import User
from app.models.actors import Actor, actors_movies
from app.models.directors import Director, director_movies
from app.models.genre import Genre, genres_movies
from app. models.movies import Movies
