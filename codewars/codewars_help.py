from requests_html import HTMLSession
import requests
import json
import re

import environ
env = environ.Env()
environ.Env.read_env()

token = env("token")

def get_codewars_help(url, num_leaders: int):
    '''
    scrape codewars leaderboard and find related GitHub repos 
    '''
    session = HTMLSession()
    katas = re.compile(r'kata|codewar', re.IGNORECASE)
    filename='leader_repos.txt'

    r = session.get(url)
    names = r.html.find('.is-big a')
    usernames = [name.text for name in names]
    for username in usernames[:num_leaders]:
        r = requests.get(f'https://api.github.com/users/{username}/repos?per_page=100', 
        headers={
            'Authorization': f'token {token}'
        })
        if r.status_code == 200:
            repos = json.loads(r.text)
            for repo in repos:
                if katas.findall(repo['html_url']):
                    with open(filename, 'a') as f:
                        f.write(f"{repo['html_url']}\n")

url = "https://www.codewars.com/users/leaderboard"

get_codewars_help(url, 25)