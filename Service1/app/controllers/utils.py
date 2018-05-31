"""Docstring."""

from flask.models import Movies, Actor, Director, Genre

# add movie or movies
# get movie or movies
def add_movie(title, description, year, runtime, rating, votes, revenue):
    if not all((title, description, year, runtime)):
        abort(400, message="Ensure you Are Passing Valid Arguments.")
    if Movies.query.filter_by(title=title).first() is not None:
        abort(400, message="Movie already exist.")
    try:
        movies = Movie(title=title, description=description, year=year,
                       runtime=runtime, rating=rating, votes=votes,
                       revenue=revenue)
        db.session.add(movies)
        db.session.commit()
    except Exception as e:
        abort(400, message="There is an issue adding this record")

    return "recorded added"

def get_movie(title):

# add Director or Directors
# get Director or Directors
def add_director():

def get_movie():

# add actor or actors
# get actor or actors
def add_actor():

def get_actor():

# add genere or generes
# get genere or generes
def add_genere():

def get_genere():
