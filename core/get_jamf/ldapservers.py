from core.get_jamf.get_jamf import GetJamf


class Ldapservers(GetJamf):

    url = '/ldapservers'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

    def by_name(self, name):
        self.url = f"{self.url}/name/{name}"
        return self.get_jamf()

    def by_id_user(self, id, user):
        self.url = f"{self.url}/id/{id}/user/{user}"
        return self.get_jamf()

    def by_id_group(self, id, group):
        self.url = f"{self.url}/id/{id}/group/{group}"
        return self.get_jamf()

    def by_(self, id, group, user):
        self.url = f"{self.url}/id/{id}/group/{group}/user/{user}"
        return self.get_jamf()

