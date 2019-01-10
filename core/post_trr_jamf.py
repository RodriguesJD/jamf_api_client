from requests.auth import HTTPBasicAuth
import requests
import time
from core import get_trr_jamf
from core.secret.key import key, username


def post_trr_jamf(url: str, post_xml: str):
    return requests.post(f'https://therealreal.jamfcloud.com/JSSResource{url}',
                        auth=HTTPBasicAuth(username, key), headers={'Content-Type': 'application/xml'}, data=post_xml)


def create_computer_group(new_group_name: str):
    """ Computer group 0 is the default for jamf to auto assign the real group id number"""
    post_xml = f"<computer_group><id>0</id><name>{new_group_name}</name><is_smart>false" \
        f"</is_smart><site><id>-1</id><name>None</name></site></computer_group>"
    url = f'/computergroups/id/0'
    return post_trr_jamf(url=url, post_xml=post_xml)

