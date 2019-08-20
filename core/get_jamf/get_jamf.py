from requests.auth import HTTPBasicAuth
import requests
import os

class GetJamf:

    key = os.environ["JAMF_KEY"]
    username = os.environ["JAMF_USERNAME"]
    base_url = os.environ["JAMF_URL_PROD"]
    url = None

    def get_jamf(self):
        return requests.get(f'{self.base_url}{self.url}',
                            auth=HTTPBasicAuth(self.username, self.key), headers={'Accept': 'application/json'})