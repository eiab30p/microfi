"""
Manage is what we are calling to run the applicationself.

The purpose of this is to set up manager, migrate, SQLAlchemy, and Secuirty

* Manager: This is an easier way to track all commands and handles how they are
           called.
* Migrate: This is use to detect changes in our ORM and upgrade or downgrade
           our database.
* SQLAlchemy: This is our ORM
* Secuirty: This assist in adding security mechanisms to the app
    * Session Based Authentication
    * Role Management
    * HTTP Authentication
    * Token Based Authentication
    * Token based password recovery / resetting
    * User registration
    * Login tracking1


Funcations:
* create_user: Just as a default user for example user
               (This will need to be for PIV) and removed for Prod
* make_shell_context: This makes a flask shell to test out queries and other
                      app related commands.

Classes:
* DBInit:This creates the DB and other models creaded in the SQLModel Folder
* DBRegUser: This is another command to create 2 users in the DB mostly for
             testing.

"""
from flask_script import Shell, Command, Server
from flask_migrate import MigrateCommand
from app import app, db, manager


def make_shell_context():
    """DocString."""
    return dict(app=app, db=db)


class DBInit(Command):
    """Creates tables from SQLAlchemy models."""

    def __init__(self, db):
        """DocString."""
        self.db = db

    def run(self):
        """DocString."""
        self.db.create_all()


# Command line options after python mange.py
manager.add_command('runserver', Server(host='127.0.0.1', port=5000))
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
