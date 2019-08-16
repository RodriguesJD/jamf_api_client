from core.get_jamf.get_jamf import GetJamf


class Accounts(GetJamf):

    url = '/accounts'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

    def by_userid(self, id):
        self.url = f"{self.url}/userid/{id}"
        return self.get_jamf()

    def by_username(self, name):
        self.url = f"{self.url}/username/{name}"
        return self.get_jamf()

    def by_groupid(self, id):
        self.url = f"{self.url}/groupid/{id}"
        return self.get_jamf()

    def by_groupname(self, name):
        self.url = f"{self.url}/groupname/{name}"
        return self.get_jamf()

