import requests
from requests.auth import HTTPBasicAuth

from env import config

headers = {
"X-Cisco-Meraki-API-Key": config['MERAKI_KEY']
}

orgs_url = f"{config['MERAKI_BASE_URL']}/organizations"
resp = requests.get(orgs_url, headers=headers)


for item in resp.json():
    print("Organization: " + item['id'] + item['name'] + "\n")