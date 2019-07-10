from core.get_jamf.get_jamf import GetJamf


class Computercommands(GetJamf):

    url = '/computercommands'

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_uuid(self, uuid):
        self.url = f"{self.url}/uuid/{uuid}"
        return self.get_jamf()

    def by_status(self, statusuuid):
        self.url = f"{self.url}/status/{statusuuid}"
        return self.get_jamf()

    def by_name(self, name):
        self.url = f"{self.url}/name/{name}"
        return self.get_jamf()

