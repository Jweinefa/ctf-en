import requests
import json
from requests.auth import HTTPBasicAuth

from env import config

headers = {
    "X-Cisco-Meraki-API-Key": config['MERAKI_KEY']
}

orgs_url = f"{config['MERAKI_BASE_URL']}/organizations"
organizations = requests.get(orgs_url, headers=headers)

for org in organizations.json():
    if org["name"] == "DevNet Sandbox":
        org_id = org["id"]


getnetworks_url = f"{config['MERAKI_BASE_URL']}/organizations/{org_id}/networks"

networks = requests.get(getnetworks_url, headers=headers)

#print(resp.json())
#print("organization:" + str(resp.json()[0]) + "\n") 

for item in networks.json():
    if item["name"] == 'DevNet Sandbox ALWAYS ON':
        network_id =item["id"]

getdevices_url = f"{config['MERAKI_BASE_URL']}/networks/{network_id}/devices"

devices = requests.get(getdevices_url, headers=headers)

#print(devices.json())



devices_list = []
for device in devices.json():
    device_dict = {}
    if "name" in device:
        device_dict["name"] = device["name"]
    if "mac" in device:
        device_dict["mac"] = device["mac"]
    if "type" in device:
        device_dict["type"] = device["type"]
    if "serial" in device:
        device_dict["serial"] = device["serial"]
    devices_list.append(device_dict)

with open("stage1.json", "w") as outfile:
    json.dump(devices_list, outfile)