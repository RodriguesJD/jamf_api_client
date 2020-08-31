from jamf_api_client.core.get_jamf.get_jamf import GetJamf


class Computerapplicationusage(GetJamf):

    url = '/computerapplicationusage'

    def by_id_and_dates(self, id, start_date, end_date):
        self.url = f"{self.url}/id/{id}/{start_date}_{end_date}"
        return self.get_jamf()

    def by_name_and_dates(self, name, start_date, end_date):
        self.url = f"{self.url}/name/{name}/{start_date}_{end_date}"
        return self.get_jamf()

    def by_udid_and_dates(self, udid, start_date, end_date):
        self.url = f"{self.url}/udid/{udid}/{start_date}_{end_date}"
        return self.get_jamf()

    def by_serialnumber_and_dates(self, serialnumber, start_date, end_date):
        self.url = f"{self.url}/serialnumber/{serialnumber}/{start_date}_{end_date}"
        return self.get_jamf()

    def by_macaddress_and_dates(self, macaddress, start_date, end_date):
        self.url = f"{self.url}/macaddress/{macaddress}/{start_date}_{end_date}"
        return self.get_jamf()

