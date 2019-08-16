from core.get_jamf.get_jamf import GetJamf


class Jssuser(GetJamf):

    url = '/jssuser'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

