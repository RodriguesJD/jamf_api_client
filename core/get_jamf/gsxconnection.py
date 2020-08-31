from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Gsxconnection(GetJamf):

    url = '/gsxconnection'

    def base_info(self):
        self.url = f"{self.url}"
        return self.get_jamf()

