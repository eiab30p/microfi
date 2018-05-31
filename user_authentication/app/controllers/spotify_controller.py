"""Docstring."""
from app import app


def generate_spotify_auth_url():
    """Docstring."""
    auth_query_parameters = {
        'response_type': 'code',
        'redirect_uri': app.config.get('REDIRECT_URI'),
        'scope': app.config.get('SCOPE'),
        'state': app.config.get('STATE'),
        'client_id': app.config.get('CLIENT_ID')
    }

    #  We are looping through the dictionary above to put it ina dirty
    #  url format. I hate it but it works for this case...
    url_params = '&'.join(['{}={}'.format(key,  val)
                          for key, val in auth_query_parameters.items()])

    # We are going to stick the auth url to the params together
    auth_url = '{}/?{}'.format(app.config.get('SPOTIFY_AUTH_URL'),
                               url_params)

    return auth_url
