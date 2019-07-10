from core.get_jamf.get_jamf import GetJamf


class Webhooks(GetJamf):

    url = '/webhooks'

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_name(self, name):
        self.url = f"{self.url}/name/{name}"
        return self.get_jamf()
