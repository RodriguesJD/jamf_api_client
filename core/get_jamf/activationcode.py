from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Activationcode(GetJamf):

    url = '/activationcode'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

