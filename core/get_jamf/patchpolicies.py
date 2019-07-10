from core.get_jamf.get_jamf import GetJamf


class Patchpolicies(GetJamf):

    url = '/patchpolicies'

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_id_subset(self, id, subset):
        self.url = f"{self.url}/id/{id}/subset/{subset}"
        return self.get_jamf()

    def by_softwaretitleconfigid(self, softwaretitleconfigid):
        self.url = f"{self.url}/softwaretitleconfig/id/{softwaretitleconfigid}"
        return self.get_jamf()

