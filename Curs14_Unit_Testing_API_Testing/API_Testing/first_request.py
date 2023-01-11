from pprint import pprint

import requests

response = requests.get('https://randomuser.me/api')

print(response.status_code)
pprint(response.text)

r_json = response.json()
print(r_json['results'][0]['gender'])

first_result = r_json['results'][0]

print(first_result['name'], first_result['email'])
