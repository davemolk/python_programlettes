import requests
import json

import environ
env = environ.Env()
environ.Env.read_env()

token = env("token")
num_results = 100
r = requests.get(f'https://api.github.com/search/repositories?q=codewarin:name&per_page={num_results}', 
            headers={'Authorization': f'token {token}'
        })

filename = "search_results.txt"
if r.status_code == 200:
    repos = json.loads(r.text)
    for repo in repos['items']:
        with open(filename, 'a') as f:
            f.write(f"{repo['html_url']}\n")


# see if i get diff results for codewars, codewar, katas, kata and make multiple calls (i guess) 
# to get all the results, then make a set from the urls and then do another search
# function of file names within each (and this is where input would be)