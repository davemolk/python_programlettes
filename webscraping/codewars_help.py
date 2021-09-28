from requests_html import HTMLSession
import requests
import json
import re

import environ
env = environ.Env()
environ.Env.read_env()

token = env("token")

def scrape_codewars_usernames(url, num: int):
    # scrape top 500 usernames on codewars leaderboard
    session = HTMLSession()
    katas = re.compile(r'kata|codewar', re.IGNORECASE)
    filename='kata_repos.txt'

    r = session.get(url)
    names = r.html.find('.is-big a')
    usernames = [name.text for name in names]
    for username in usernames[:num]:
        r = requests.get(f'https://api.github.com/users/{username}/repos?per_page=100', 
        headers={
            'Authorization': 'token {}'.format(token)
        })
        if r.status_code == 200:
            repos = json.loads(r.text)
            for repo in repos:
                if katas.findall(repo['url']):
                    with open(filename, 'a') as f:
                        f.write(f"{repo['url']}\n")

url = "https://www.codewars.com/users/leaderboard"

scrape_codewars_usernames(url, 5)