import csv
from core import get_trr_jamf


class RetouchingAnalyzation:
    """
    This class queries the jamf static group titled 'Retouching - static group' its id # is 154. Then parses the queried
    data and pull the data that is relevant to the Retouching and IT department.

    Going forward TRR is going to set standard versions for the OS and its applications. This class will show all the
    retouching devices and there current os and application versions.
    """

    group_id = 154
    
    @staticmethod
    def parse_applications(application_data: dict) -> list:
        """
        This takes the application_data dict and parses out the relevant application data for this project.

        Parameters
        ----------
        application_data
            dict

        Returns
        -------
        app_list
            list

        """
        bridge = ''
        bridge_version = ''
        lightroom = ''
        lightroom_version = ''
        photoshop = ''
        photoshop_version = ''
        colorchecker = ''
        colorchecker_version = ''
        colormunki = ''
        colormunki_version = ''
        i1Profiler = ''
        i1Profiler_version = ''
        i1ProfilerTray = ''
        i1ProfilerTray_version = ''
        wacom = ''
        wacom_version = ''

        for application in application_data:
            app_name = application['name']
            app_version = application['version']
            if 'Adobe Bridge' in app_name:
                bridge = app_name
                bridge_version = app_version
            elif 'Adobe Lightroom' in app_name:
                lightroom = app_name
                lightroom_version = app_version
            elif 'Adobe Photoshop' in app_name:
                photoshop = app_name
                photoshop_version = app_version
            elif 'ColorChecker Passport.app' in app_name:
                colorchecker = app_name
                colorchecker_version = app_version
            elif 'ColorMunki' in app_name:
                colormunki = app_name
                colormunki_version = app_version
            elif "i1Profiler.app" in app_name:
                i1Profiler = app_name
                i1Profiler_version = app_version
            elif 'i1ProfilerTray.app' in app_name:
                i1ProfilerTray = app_name
                i1Profiler_version = app_version
            elif 'Wacom Tablet Utility.app' in app_name:
                wacom = app_name
                wacom_version = app_version
            else:
                pass

        app_list = [bridge, bridge_version,
                    lightroom, lightroom_version,
                    photoshop, photoshop_version,
                    colorchecker, colorchecker_version,
                    colormunki, colormunki_version,
                    i1Profiler, i1Profiler_version,
                    i1ProfilerTray, i1ProfilerTray_version,
                    wacom, wacom_version]

        return app_list

    def parse_computer_data(self, computer_data: list) -> list:
        """
        This function takes each dict from inside the computer_data list and pulls out relevant data for this project.
        Parameters
        ----------
        computer_data
            list

        Returns
        -------
        parsed_comp_list
            list

        """
        parsed_comp_list = []
        for computer in computer_data:
            hostname = computer['computer']['general']['name']
            serial_number = computer['computer']['general']['serial_number']
            model = computer['computer']['hardware']['model']
            os_version = computer['computer']['hardware']['os_version']
            applications = computer['computer']['software']['applications']

            parsed_app_data = self.parse_applications(applications)

            bridge = parsed_app_data[0]
            bridge_version = parsed_app_data[1]
            lightroom = parsed_app_data[2]
            lightroom_version = parsed_app_data[3]
            photoshop = parsed_app_data[4]
            photoshop_version = parsed_app_data[5]
            colorchecker = parsed_app_data[6]
            colorchecker_version = parsed_app_data[7]
            colormunki = parsed_app_data[8]
            colormunki_version = parsed_app_data[9]
            i1Profiler = parsed_app_data[10]
            i1Profiler_version = parsed_app_data[11]
            i1ProfilerTray = parsed_app_data[12]
            i1ProfilerTray_version = parsed_app_data[13]
            wacom = parsed_app_data[14]
            wacom_version = parsed_app_data[15]

            retouching_comp_data = [hostname, serial_number, model, os_version, bridge, bridge_version, lightroom,
                                    lightroom_version, photoshop, photoshop_version, colorchecker, colorchecker_version,
                                    colormunki, colormunki_version, i1Profiler, i1Profiler_version, i1ProfilerTray,
                                    i1ProfilerTray_version, wacom, wacom_version]
            parsed_comp_list.append(retouching_comp_data)

        return parsed_comp_list

    # TODO move computers_in_group func to group_data_core
    @staticmethod
    def computers_in_group(computer_group: dict) -> list:
        """
        This function takes a dict of static group 154 and returns list of all computers in the group.
        Parameters
        ----------
        computer_group
            dict

        Returns
        -------
        comp_data_in_group
            list
        """
        comp_data_in_group = []
        computers = computer_group['computer_group']['computers']
        for computer in computers:
            comp_id = computer['id']
            computer_data = get_trr_jamf.computer_by_id(comp_id).json()
            comp_data_in_group.append(computer_data)

        return comp_data_in_group

    def retouching_static_group(self) -> object:
        """
        Request the group data from JAMF of the group named 'Retouching - static group'.
        'Retouching - static group's id is 154

        Returns
        -------
        group_data
            requests.models.Response
        """
        group_data = get_trr_jamf.computergroup_by_id(str(self.group_id))
        return group_data

    def main(self) -> list:
        """
        This function queries the jamf static group titled 'Retouching - static group' its id # is 154. Then parses the
        queried data and returns the data that is relevant to the Retouching and IT department.

        Returns
        -------
        parsed_retouching
            list
        """
        retouching_staticgroup = self.retouching_static_group().json()  # Query jamf for static group id number 154.
        computer_data = self.computers_in_group(retouching_staticgroup)  # Query jamf for all computers in static group.
        parsed_retouching = self.parse_computer_data(computer_data)  # Computer data that is relevant to retouching.

        return parsed_retouching


def retouching_analyzation_to_csv():
    post_parse_retouching = RetouchingAnalyzation().main()
    with open('parsed_retouching.csv', mode='w') as retouch_file:
        retouching_writer = csv.writer(retouch_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        line_count = 0
        for parsed_station in post_parse_retouching:
            if line_count == 0:
                header_list = ['hostname', 'serial_number', 'model', 'os_version', 'bridge', 'bridge_version',
                               'lightroom', 'lightroom_version', 'photoshop', 'photoshop_version', 'colorchecker',
                               'colorchecker_version', 'colormunki', 'colormunki_version', 'i1Profiler',
                               'i1Profiler_version', 'i1ProfilerTray', 'i1ProfilerTray_version', 'wacom',
                               'wacom_version']
                retouching_writer.writerow(header_list)
                retouching_writer.writerow(parsed_station)
                line_count += 1
            else:
                retouching_writer.writerow(parsed_station)


retouching_analyzation_to_csv()
