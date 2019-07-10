from core.get_jamf.get_jamf import GetJamf


class Users(GetJamf):

    url = '/users'

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_name(self, name):
        self.url = f"{self.url}/name/{name}"
        return self.get_jamf()

    def by_email(self, email):
        self.url = f"{self.url}/email/{email}"
        return self.get_jamf()

