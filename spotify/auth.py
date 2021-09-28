import requests
import base64
import datetime

import environ
env = environ.Env()
environ.Env.read_env()

client_id = env("client_id")
client_secret = env("client_secret")
client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode())

token_url = 'https://accounts.spotify.com/api/token'
method = 'POST'
token_data = {
    "grant_type": "client_credentials",
}
token_headers = {
    "Authorization": f"Basic {client_creds_b64.decode()}",
}

r = requests.post(token_url, data=token_data, headers=token_headers)
valid_request = r.status_code in range(200, 299)

if valid_request:
    token_response_data = r.json()
    now = datetime.datetime.now()
    access_token = token_response_data['access_token']
    expires_in = token_response_data['expifres_in']
    expires = now + datetime.timedelta(seconds=expires_in)
    did_expire = expires < now
