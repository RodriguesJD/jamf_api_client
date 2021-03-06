from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Computermanagement(GetJamf):

    url = '/computermanagement'

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_name(self, name):
        self.url = f"{self.url}/name/{name}"
        return self.get_jamf()

    def by_udid(self, udid):
        self.url = f"{self.url}/udid/{udid}"
        return self.get_jamf()

    def by_serialnumber(self, serialnumber):
        self.url = f"{self.url}/serialnumber/{serialnumber}"
        return self.get_jamf()

    def by_macaddress(self, macaddress):
        self.url = f"{self.url}/macaddress/{macaddress}"
        return self.get_jamf()

    def by_id_subset(self, id, subset):
        self.url = f"{self.url}/id/{id}/subset/{subset}"
        return self.get_jamf()

    def by_id_username(self, id, username):
        self.url = f"{self.url}/id/{id}/username/{username}"
        return self.get_jamf()

    def by_(self, id, username, subset):
        self.url = f"{self.url}/id/{id}/username/{username}/subset/{subset}"
        return self.get_jamf()

    def by_id_filter(self, id, filter):
        self.url = f"{self.url}/id/{id}/patchfilter/{filter}"
        return self.get_jamf()

