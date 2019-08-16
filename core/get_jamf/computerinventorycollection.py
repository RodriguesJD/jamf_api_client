from core.get_jamf.get_jamf import GetJamf


class Computerinventorycollection(GetJamf):

    url = '/computerinventorycollection'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

