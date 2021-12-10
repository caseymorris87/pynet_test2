import os
import requests
from rich import print
from urllib3.exceptions import InsecureRequestWarning

# Ignore insecure warings for sites with self-signed certificates
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


url = "https://netbox.lasthop.io/api/dcim/devices"

token = os.environ['NETBOX_TOKEN']

token = f'Token {token}'

headers = {
    "accept": "application/json; version=2.4;",
    "authorization": token,
}

response = requests.get(url, headers=headers, verify=False)
response = response.json()

print()
print(response)
print()

