from core.get_jamf.get_jamf import GetJamf


class Byoprofiles(GetJamf):

    url = '/byoprofiles'

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_name(self, name):
        self.url = f"{self.url}/name/{name}"
        return self.get_jamf()

    def by_sitename(self, siteName):
        self.url = f"{self.url}/site/name/{siteName}"
        return self.get_jamf()

    def by_siteid(self, siteId):
        self.url = f"{self.url}/site/id/{siteId}"
        return self.get_jamf()

