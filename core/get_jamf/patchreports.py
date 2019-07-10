from core.get_jamf.get_jamf import GetJamf


class Patchreports(GetJamf):

    # TODO block this object from being used without using a search func.

    url = '/patchreports'

    def by_patchsoftwaretitleid(self, id):
        self.url = f"{self.url}/patchsoftwaretitleid/{id}"
        return self.get_jamf()

    def by_patchsoftwaretitleid_version(self, id, version):
        self.url = f"{self.url}/patchsoftwaretitleid/{id}/version/{version}"
        return self.get_jamf()

