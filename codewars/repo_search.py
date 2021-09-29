import requests
import json

import environ
env = environ.Env()
environ.Env.read_env()

token = env("token")

# max is 100
num_results = 10
queries = ['codewar', 'codewars', 'kata', 'katas']
filename_all = 'all_katas.txt'
filename_set = 'kata_set.txt'

for query in queries:
    r = requests.get(f'https://api.github.com/search/repositories?q={query}in:name&per_page={num_results}', 
                headers={'Authorization': f'token {token}'
            })

    if r.status_code == 200:
        repos = json.loads(r.text)
        for repo in repos['items']:
            with open(filename_all, 'a') as f:
                f.write(f"{repo['html_url']}\n")

with open(filename_all) as f:
    lines = f.readlines()   
    kata_set = set(lines)
    for kata in kata_set:
        with open(filename_set, 'a') as f:
            f.write(f"{kata}")
