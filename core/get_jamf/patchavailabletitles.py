from core.get_jamf.get_jamf import GetJamf


class Patchavailabletitles(GetJamf):

    # TODO block this object from being used without using a search func.

    url = '/patchavailabletitles'

    def by_sourceid(self, id):
        self.url = f"{self.url}/sourceid/{id}"
        return self.get_jamf()

