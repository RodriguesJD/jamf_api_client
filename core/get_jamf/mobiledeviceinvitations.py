from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Mobiledeviceinvitations(GetJamf):

    url = '/mobiledeviceinvitations'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_invitation(self, invitation):
        self.url = f"{self.url}/invitation/{invitation}"
        return self.get_jamf()

