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
    for kata in katas:
        kata['completedLanguages'] = ', '.join(kata['completedLanguages'])
        try:
            r = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{kata['id']}")
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            # TODO
            # flash error message and add redirect 
            print(err)
        data = r.json()

        kata['description'] = data['description']
        kata['tags'] = ', '.join(data['tags'])
        kata['rank']= data['rank']['name']
        kata['url'] = data['url'] + '/solutions/'
        if kata['url'] == 'https://www.codewars.com/kata/58279e13c983ca4a2a00002a/solutions/':
            print(kata)
