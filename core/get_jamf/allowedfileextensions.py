from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Allowedfileextensions(GetJamf):

    url = '/allowedfileextensions'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_extension(self, extension):
        self.url = f"{self.url}/extension/{extension}"
        return self.get_jamf()

