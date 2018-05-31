'''
Configuration File.

The Configuration is simply going to set up your basic needs. For this example
we are going to enable cross-site request forgery or CSRF. This helps with
prevention of unauthorized commands to be transmitted from the app.

The SECRET_KEY is in fact redicoulse for a reason but it is only needed when
CSRF is enabled, and is used to create a cryptographic token that is used to
validate a form.

It is better seperate other configs to Dev,Test,Prod. This doesn't make sense
for me since everything is based in the .env file.
'''
from os.path import join, dirname
from dotenv import load_dotenv
import os


class Config(object):
    '''docstring stuff.'''

    # Reding from a .env file for environment variables
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path, verbose=True)

    WTF_CSRF_ENABLED = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_REGISTERABLE = True
    SECURITY_TOKEN_MAX_AGE = 600  # 10 minutes, default: None
    SECURITY_PASSWORD_SALT = os.environ.get('SECRET_KEY')
    # email server
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # Database connection and Repo Migration
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQL_TYPE') + '://'\
        + os.environ.get('SQL_USERNAME') + ':'\
        + os.environ.get('SQL_PASSWORD') + '@' \
        + os.environ.get('SQL_IP') + '/' + os.environ.get('SQL_DBNAME') + ''

    SQLALCHEMY_MIGRATE_REPO = join(dirname(__file__), 'db_repository')

    CLIENT_ID = '61729cecf8fc474b8ef6ca2dfeb8ae55'
    CLIENT_SECRET = '324dfe79900d4277baaa9eba4a8d87a0'

    # Spotify URLS
    SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
    SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
    SPOTIFY_API_BASE_URL = 'https://api.spotify.com'
    API_VERSION = 'v1'
    SPOTIFY_API_URL = '{}/{}'.format(SPOTIFY_API_BASE_URL, API_VERSION)

    # Server-side Parameters
    CLIENT_SIDE_URL = 'http://127.0.0.1'
    PORT = 5001
    REDIRECT_URI = '{}:{}/callback/q'.format(CLIENT_SIDE_URL, PORT)
    SCOPE = 'user-read-private user-read-email'
    STATE = '34fFs29kd09'
    SHOW_DIALOG_bool = True
    SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()
