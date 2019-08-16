from core.get_jamf.get_jamf import GetJamf


class Mobiledeviceapplications(GetJamf):

    url = '/mobiledeviceapplications'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_bundleid(self, bundleid):
        self.url = f"{self.url}/bundleid/{bundleid}"
        return self.get_jamf()

    def by_bundleid_version(self, bundleid, version):
        self.url = f"{self.url}/bundleid/{bundleid}/version/{version}"
        return self.get_jamf()

    def by_name(self, name):
        self.url = f"{self.url}/name/{name}"
        return self.get_jamf()

    def by_id_subset(self, id, subset):
        self.url = f"{self.url}/id/{id}/subset/{subset}"
        return self.get_jamf()

