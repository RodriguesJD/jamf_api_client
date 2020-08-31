from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Peripheraltypes(GetJamf):

    url = '/peripheraltypes'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

