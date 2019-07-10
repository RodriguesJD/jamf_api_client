from core.get_jamf.get_jamf import GetJamf


class Patches(GetJamf):

    url = '/patches'

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_name(self, name):
        self.url = f"{self.url}/name/{name}"
        return self.get_jamf()

    def by_id_version(self, id, version):
        self.url = f"{self.url}/id/{id}/version/{version}"
        return self.get_jamf()

