import requests
from rich import print

URL = 'https://netbox.lasthop.io/api'
HEADERS = {"accept": "application/json; version=2.4;"}

response = requests.get(URL, HEADERS, verify=False)

print(dir(response))
print()
print()
print()
print(response.json())
print()
print(response.text)
print()
print(response.status_code)
print()
print(response.ok)
