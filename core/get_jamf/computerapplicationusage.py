from core.get_jamf.get_jamf import GetJamf


class Computerapplicationusage(GetJamf):

    # TODO block this object from being used without using a search func.

    url = '/computerapplicationusage'

    def by_id_id(self, id, start_date_end_date):
        self.url = f"{self.url}/id/{id}/{start_date_end_date}"
        return self.get_jamf()

    def by_name_name(self, name, start_date_end_date):
        self.url = f"{self.url}/name/{name}/{start_date_end_date}"
        return self.get_jamf()

    def by_udid_udid(self, udid, start_date_end_date):
        self.url = f"{self.url}/udid/{udid}/{start_date_end_date}"
        return self.get_jamf()

    def by_serialnumber_serialnumber(self, serialnumber, start_date_end_date):
        self.url = f"{self.url}/serialnumber/{serialnumber}/{start_date_end_date}"
        return self.get_jamf()

    def by_macaddress_macaddress(self, macaddress, start_date_end_date):
        self.url = f"{self.url}/macaddress/{macaddress}/{start_date_end_date}"
        return self.get_jamf()

