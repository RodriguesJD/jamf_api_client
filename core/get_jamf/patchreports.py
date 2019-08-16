from core.get_jamf.get_jamf import GetJamf


class Patchreports(GetJamf):

    url = '/patchreports'

    def by_patchsoftwaretitleid(self, id):
        self.url = f"{self.url}/patchsoftwaretitleid/{id}"
        return self.get_jamf()

    def by_id_version(self, id, version):
        self.url = f"{self.url}/patchsoftwaretitleid/{id}/version/{version}"
        return self.get_jamf()

