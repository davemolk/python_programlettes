import requests

def katas(username):
    url = f"https://www.codewars.com/api/v1/users/{username}/code-challenges/completed?"
    
    # r = requests.get(url)
    # if r.status_code in range(200, 299):
    #     data = r.json()
    #     katas = (data['data'])
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    
    data = r.json()
    katas = data['data']

    # print(katas)
    for kata in katas:
        # print(kata['id'])
    # for kata in katas:
        r = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{kata['id']}")
        if r.status_code in range(200, 299):
            data = r.json()
            print(data['name'])
            # katas_info = data['data']
            # print(katas_info)

    
katas('davemolk')