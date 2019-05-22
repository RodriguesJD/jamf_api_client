from requests.auth import HTTPBasicAuth
import requests
# https://developer.jamf.com/apis/jamf-pro-api/index
from core.secret.key import key, username
from pprint import pprint


class GetTrrJamf:

    url = None

    def get_trr_jamf(self):
        """therealreal prod"""
        return requests.get(f'https://therealreal.jamfcloud.com/JSSResource{self.url}',
                            auth=HTTPBasicAuth(username, key), headers={'Accept': 'application/json'})

    def by_name(self, name):
        self.url = f"{self.url}/name/{name}"
        return self.get_trr_jamf()

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_trr_jamf()

    def all(self):
        all_items = []
        first_key = list(self.get_trr_jamf().json().keys())[0]
        for item in self.get_trr_jamf().json()[first_key]:
            item_id = item['id']
            items_data = self.by_id(item_id)
            first_item_key = list(items_data.json().keys())[0]
            parsed_item = items_data.json()[first_item_key]
            all_items.append(parsed_item)
            self.url = self.url.split("/id")[0]

        return all_items

