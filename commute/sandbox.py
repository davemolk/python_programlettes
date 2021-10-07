import requests
import pprint
import json
import environ
env = environ.Env()
environ.Env.read_env()

KEY = env("KEY")
START = env("START")
END = env("END")

base_url = 'http://www.mapquestapi.com/directions/v2/route'

r = requests.get(f'{base_url}?key={KEY}&{START}&{END}')
# pprint.pprint(r.json())
data = r.json()
# pprint.pprint(data['route'])
print(data['route']['realTime'])