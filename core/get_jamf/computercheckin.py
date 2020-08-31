from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Computercheckin(GetJamf):

    url = '/computercheckin'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

