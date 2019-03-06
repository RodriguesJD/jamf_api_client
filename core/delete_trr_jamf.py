from requests.auth import HTTPBasicAuth
import requests
import time

from core.secret.key import key, username
from core import get_trr_jamf


def delete_trr_jamf(url: str, delete_xml: str):
    return requests.delete(f'https://therealreal.jamfcloud.com/JSSResource{url}',
                           auth=HTTPBasicAuth(username, key), headers={'Content-Type': 'application/xml'},
                           data=delete_xml)


def delete_computer_group(group_id: str):
    group_name = get_trr_jamf.computergroup_by_id(computergroup_id=f"{group_id}").json()['computer_group']['name']
    """ Computer group 0 is the default for jamf to auto assign the real group id number"""
    delete_xml = f"<computer_group><id>{group_id}</id><name>{group_name}</name><is_smart>false" \
        f"</is_smart><site><id>-1</id><name>None</name></site></computer_group>"
    url = f'/computergroups/id/{group_id}'

    return delete_trr_jamf(url=url, delete_xml=delete_xml)


