import json
import requests

import environ
env = environ.Env()
environ.Env.read_env()

token = env("token")

filename = 'repos.txt'
base_url = 'https://api.github.com/users/GiacomoSorbi/repos?per_page=100'
r = requests.get(base_url, 
    headers={
        'Authorization': 'token {}'.format(token)
    })
print(r.json())

# projects = []
# repos = json.loads(r.text)
# for repo in repos:
#     # with open(filename, 'a') as f:
#     #     f.write(f"{repo['url']}\n")
#     projects.append(repos)
#     print(repo['url'])

# print(projects)


