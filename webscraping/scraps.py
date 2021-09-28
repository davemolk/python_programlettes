from requests_html import HTMLSession
import requests
import json
import re

import environ
env = environ.Env()
environ.Env.read_env()

token = env("token")

def scrape_codewars_usernames(url, num: int, filename='all_repos.txt'):
    # scrape top 500 usernames on codewars leaderboard
    session = HTMLSession()
    projects = []
    katas = re.compile(r'kata|codewar', re.IGNORECASE)

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
                print(repo['url'])
                if katas.findall(repo['url']):
                    with open(filename, 'a') as f:
                        f.write(f"{repo['url']}\n")
                    projects.append(repo['url'])


url = "https://www.codewars.com/users/leaderboard"

print(scrape_codewars_usernames(url, 5, 'codewars_usernames2.txt'))





# def scrape_codewars_usernames(url, filename='codewars_usernames.txt', save=False):
#     session = HTMLSession()
#     r = session.get(url)
#     names = r.html.find('.is-big a')
#     usernames = [name.text for name in names]
#     if save:
#         for username in usernames:
#             with open(filename, 'a') as f:
#                 f.write(f"{username}\n")
#     return usernames



# url = "https://www.codewars.com/users/leaderboard"

# print(scrape_codewars_usernames(url, 'codewars_usernames2.txt', True))

# scrape usernames of top 500 on codewars leaderboard
'''
names = r.html.find('.is-big a')
usernames = []
filename1 = 'codewars.txt'
for name in names:
    with open(filename1, 'a') as f:
        f.write(f"{name.text}\n")
    usernames.append(name.text)
'''

# # print(usernames)

'''
# scrape repos for each user
projects = []
filename2 = 'all_repos.txt'
for username in usernames:
    r = requests.get(f'https://api.github.com/users/{username}/repos?per_page=100', 
    headers={
        'Authorization': 'token {}'.format(token)
    })
    if r.status_code == 200:
        repos = json.loads(r.text)
        for repo in repos:
            with open(filename2, 'a') as f:
                f.write(f"{repo['url']}\n")
            projects.append(repo['url'])
            
'''

'''
filename3 = 'katas.txt'
katas = re.compile(r'kata|codewar', re.IGNORECASE)
with open('all_repos.txt') as f:
    lines = f.readlines()

for line in lines:
    match = katas.findall(line)
    if match:
        with open(filename3, 'a') as f:
            f.write(f'{line}')

'''

# match = katas.findall('https://api.github.com/repos/myjinxin2015/Katas-list-of-Training-JS-series')
# print(match)

