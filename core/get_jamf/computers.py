from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Computers(GetJamf):

    url = '/computers'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

    def by_subset(self, basic):
        self.url = f"{self.url}/subset/basic"
        return self.get_jamf()

    def by_match(self, match):
        self.url = f"{self.url}/match/{match}"
        return self.get_jamf()

    def by_match_name(self, matchname):
        self.url = f"{self.url}/match/name/{matchname}"
        return self.get_jamf()

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

