from core.get_jamf.get_jamf import GetJamf


class Policies(GetJamf):

    url = '/policies'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_name(self, name):
        self.url = f"{self.url}/name/{name}"
        return self.get_jamf()

    def by_id_subset(self, id, subset):
        self.url = f"{self.url}/id/{id}/subset/{subset}"
        return self.get_jamf()

    def by_category(self, category):
        self.url = f"{self.url}/category/{category}"
        return self.get_jamf()

    def by_createdBy(self, createdBy):
        self.url = f"{self.url}/createdBy/{createdBy}"
        return self.get_jamf()

