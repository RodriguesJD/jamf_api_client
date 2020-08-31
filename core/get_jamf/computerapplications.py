from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Computerapplications(GetJamf):

    url = '/computerapplications'

    def by_application(self, application):
        self.url = f"{self.url}/application/{application}"
        return self.get_jamf()

    def by_application_inventory(self, application, inventory):
        self.url = f"{self.url}/application/{application}/inventory/{inventory}"
        return self.get_jamf()

    def by_application_version(self, application, version):
        self.url = f"{self.url}/application/{application}/version/{version}"
        return self.get_jamf()

    def by_(self, application, version, inventory):
        self.url = f"{self.url}/application/{application}/version/{version}/inventory/{inventory}"
        return self.get_jamf()

