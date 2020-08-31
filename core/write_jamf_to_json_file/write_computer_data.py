import os
import json
import datetime
from jamf_api_client.core.get_jamf.computers import Computers
from jamf_api_client.core.write_jamf_to_json_file import write_to_json_tools


class WriteJamfComputerDataToJSON:
    """
    If the jamf_computer_data_{datetime}.json file is older than 24 hours then update the file and return the filename.
    If it is less than 24 hours then dont update the json file but return the file name
    """

    base_file_name = "jamf_computer_data_"

    def _dump_data_to_json_file(self):
        print(f"Updating {self.base_file_name}*.json file. This will take a few minutes.")
        computer_dict = dict()
        for computer in Computers().base_info().json()["computers"]:
            id = computer['id']
            computer_data = Computers().by_id(id).json()
            computer_dict.update({id: computer_data})

        time_stamp = datetime.datetime.utcnow().strftime("%Y_%m_%d")
        json_file_name = f"{self.base_file_name}{time_stamp}.json"
        with open(json_file_name, "w") as write_file:
            json.dump(computer_dict, write_file)

        return json_file_name

    def main(self):
        json_needs_updating = write_to_json_tools.data_needs_updating(self.base_file_name)
        if json_needs_updating[0]:
            return self._dump_data_to_json_file()
        else:
            return list(json_needs_updating[1])[0]



