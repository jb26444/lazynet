import requests
import json
from pprint import pprint

r = requests.get('https://api.chucknorris.io/jokes/random')
r.json()

pprint(r.json())


