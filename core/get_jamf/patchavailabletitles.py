from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Patchavailabletitles(GetJamf):

    url = '/patchavailabletitles'

    def by_sourceid(self, id):
        self.url = f"{self.url}/sourceid/{id}"
        return self.get_jamf()

