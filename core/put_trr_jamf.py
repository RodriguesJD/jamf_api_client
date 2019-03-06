from requests.auth import HTTPBasicAuth
import requests

from core.secret.key import key, username
from core import get_trr_jamf


def put_trr_jamf(url: str, put_xml: str):
    return requests.put(f'https://therealreal.jamfcloud.com/JSSResource{url}',
                        auth=HTTPBasicAuth(username, key), headers={'Content-Type': 'application/xml'}, data=put_xml)


def add_host_to_comp_group(group_id: str, add_host_id: str, group_name: str):
    """Add a host to a computer group. Use the computer groups id
    syntax for host is f"<computer><id>{computer_id}</id></computer>"""
    url = f"/computergroups/id/{group_id}"
    put_xml = f"<computer_group><id>{group_id}</id><name>" \
        f"{group_name}</name><computer_additions>" \
        f"{add_host_id}</computer_additions></computer_group>"

    return put_trr_jamf(url=url, put_xml=put_xml)







