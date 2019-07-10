from core.get_jamf.get_jamf import GetJamf


class Mobiledevicecommands(GetJamf):

    url = '/mobiledevicecommands'

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_uuid(self, uuid):
        self.url = f"{self.url}/uuid/{uuid}"
        return self.get_jamf()

    def by_name(self, name):
        self.url = f"{self.url}/name/{name}"
        return self.get_jamf()

    def by_command(self, command):
        self.url = f"{self.url}/command/{command}"
        return self.get_jamf()

