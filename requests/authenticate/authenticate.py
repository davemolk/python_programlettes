import requests
from bs4 import BeautifulSoup
import creds

loginurl = ('https://the-internet.herokuapp.com/authenticate')
secure_url = ('https://the-internet.herokuapp.com/secure')

payload = {
    'username': creds.username,
    'password': creds.password,
}

# authenticated request
r = requests.post(loginurl, data=payload)

# not authenticated because not using a session, so won't work (redirect to login)
r2 = requests.get(secure_url)

# print(r.text)


# keeps session open via requests sessions and using a context manager
with requests.session() as s:
    s.post(loginurl, data=payload)
    r = s.get(secure_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())