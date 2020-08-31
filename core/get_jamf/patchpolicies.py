from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Patchpolicies(GetJamf):

    url = '/patchpolicies'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_id_subset(self, id, subset):
        self.url = f"{self.url}/id/{id}/subset/{subset}"
        return self.get_jamf()

    def by_softwaretitleconfig_id(self, softwaretitleconfigid):
        self.url = f"{self.url}/softwaretitleconfig/id/{softwaretitleconfigid}"
        return self.get_jamf()

