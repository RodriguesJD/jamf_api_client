from core.get_jamf.get_jamf import GetJamf


class Peripheraltypes(GetJamf):

    url = '/peripheraltypes'

    def by_id(self, id):
        self.url = f"{self.url}/id/{id}"
        return self.get_jamf()

