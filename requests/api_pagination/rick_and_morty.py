import requests
import pandas as pd


# has great documentation which gives us a lot of this info...
base_url = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

def main_request(base_url, endpoint, x):
    r = requests.get(base_url + endpoint + f'?page={x}')
    return r.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    char_list = []
    for item in response['results']:
        char = {
            'id': item['id'],
            'name': item['name'],
            'no_ep': len(item['episode']),
        }
        char_list.append(char)
    return char_list

main_list = []

data = main_request(base_url, endpoint, 1)
for x in range(1, get_pages(data) + 1):
    print(x)
    main_list.extend(parse_json(main_request(base_url, endpoint, x)))

data_frame = pd.DataFrame(main_list)
data_frame.to_csv('char_list.csv', index=False)