"""
Spotify.

This is going to be for any Spotify Callbacks or redirectionsself.
"""
from flask import make_response, render_template, redirect, request
from flask_restful import Resource, reqparse
from app import api, app
import jwt
import requests
import json


# Callback which will set JWT with user information and Spotify information
class Callback_auth(Resource):
    """Docstring."""

    def get(self):
        """
        Auth.

        Requesting refresh and access Tokens
        """
        auth_token = request.args['code']

        url = 'https://accounts.spotify.com/api/token'

        data = {
            'grant_type': 'authorization_code',
            'code': auth_token,
            'redirect_uri': app.config.get('REDIRECT_URI'),
            'client_id': app.config.get('CLIENT_ID'),
            'client_secret': app.config.get('CLIENT_SECRET')
            }

        r = requests.post(url, data=data)

        # Auth: Tokens are Returned to Application
        response_data = json.loads(r.text)

        access_token = response_data['access_token']
        refresh_token = response_data['refresh_token']
        token_type = response_data['token_type']
        expires_in = response_data['expires_in']

        # Auth: Use the access token to access Spotify API
        authorization_header = {'Authorization':
                                'Bearer {}'.format(access_token)}

        # Get profile data
        user_profile_api_endpoint = '{}/me'.format(
                                    app.config.get('SPOTIFY_API_URL'))
        profile_response = requests.get(user_profile_api_endpoint,
                                        headers=authorization_header)
        profile_data = json.loads(profile_response.text)

        # Get user playlist data
        playlist_api_endpoint = '{}/playlists'.format(profile_data['href'])

        playlists_response = requests.get(playlist_api_endpoint,
                                          headers=authorization_header)

        playlist_data = json.loads(playlists_response.text)

        # Combine profile and playlist data to display
        display_arr = [profile_data] + playlist_data['items']

        # JWT with all data here!
        payload = jwt.decode(request.cookies.get('auth_token'),
                             app.config.get('SECRET_KEY'),
                             algorithms=['HS256'])
        print(payload)
        resp = make_response(redirect('http://127.0.0.1:5001/3'))
        # resp.set_cookie('auth_token', token.decode('utf-8'))
        return resp

# Will Need to do a refresh of a Token
api.add_resource(Callback_auth, '/callback/q')
