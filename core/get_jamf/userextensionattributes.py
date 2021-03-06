from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Userextensionattributes(GetJamf):

    url = '/userextensionattributes'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_name(self, name):
        self.url = f"{self.url}/name/{name}"
        return self.get_jamf()

