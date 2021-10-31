import requests

def katas(username):
    url = f"https://www.codewars.com/api/v1/users/{username}/code-challenges/completed?"
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    
    data = r.json()
    katas = data['data']
    first = katas[0]
    print(first['name'])
    print(first)
    # for kata in katas:
    #     try:
    #         r = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{kata['id']}")
    #         r.raise_for_status()
    #     except requests.exceptions.HTTPError as err:
    #         print(err)
    #     data = r.json()
    #     # print(data['name'])
    #     print(data['name'])

    
katas('davemolk')