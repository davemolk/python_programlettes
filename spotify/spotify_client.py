import base64
import datetime
from urllib.parse import urlencode
import pprint

import requests
import environ
env = environ.Env()
environ.Env.read_env()

client_id = env("client_id")
client_secret = env("client_secret")


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now() # will expire immediately
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token'


    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret
    
    def get_client_credentials(self):
        '''
        Return a base64 encoded string
        '''
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception("Please set client_secret and client_id")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }

    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        }
    
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 300):
            raise Exception("Could not authenticate")
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in']
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True

    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now:
            self.perform_auth()
            return self.get_access_token()
        elif token == None:
            self.perform_auth()
            return self.get_access_token()
        return token

    def get_resource_header(self):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        return headers

    def get_resource(self, lookup_id, resource_type='albums', version='v1'):
        endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}"
        headers = self.get_resource_header()
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200, 300):
            raise Exception("An error occured")
        return r.json()
    
    def get_album(self, lookup_id):
        return self.get_resource(lookup_id, resource_type='albums')

    def get_artist(self, lookup_id):
        return self.get_resource(lookup_id, resource_type='artists')

    def base_search(self, query_params, results=20):
        pp = pprint.PrettyPrinter()
        headers = self.get_resource_header()
        endpoint = "https://api.spotify.com/v1/search"
        lookup_url = f"{endpoint}?{query_params}&limit={results}"
        r = requests.get(lookup_url, headers=headers)
        if r.status_code not in range(200, 300):
            raise Exception("An error occured")
        return pp.pprint(r.json())

    def search(self, query=None, operator=None, operator_query=None, search_type='artist', results=20):
        if query == None:
            raise Exception("A query is required")
        if isinstance(query, dict):
            query = " ".join([f"{k}:{v}" for k,v in query.items()])
        if operator != None and operator_query != None:
            if operator.lower() == 'or' or operator.lower() == 'not':
                operator = operator.upper()
                if isinstance(operator_query, str):
                    query = f"{query} {operator} {operator_query}"
        query_params = urlencode({'q': query, 'type': search_type.lower()})

        return self.base_search(query_params)

spotify = SpotifyAPI(client_id, client_secret)
print(spotify.search(query="Danger", operator='NOT', operator_query="Zone", search_type='track'))