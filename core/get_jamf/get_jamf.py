from requests.auth import HTTPBasicAuth
import requests

from core.secret.key import key, username
from core import config


class GetJamf:

    url = None

    def get_jamf(self):
        return requests.get(f'{config.base_url}{self.url}',
                            auth=HTTPBasicAuth(username, key), headers={'Accept': 'application/json'})
