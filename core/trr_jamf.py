from requests.auth import HTTPBasicAuth
import requests
from pprint import pprint
from datetime import datetime
# https://developer.jamf.com/apis/jamf-pro-api/index
from core.secret.key import key, username

def trr_jamf(url: str) -> requests.models.Response:
    """therealreal prod"""
    return requests.get(f'https://therealreal.jamfcloud.com/JSSResource{url}',
                        auth=HTTPBasicAuth(username, key), headers={'Accept': 'application/json'})


# def core(url: str) -> requests.models.Response:
#     """therealreal dev"""
#     print("Jamf Dev")
#     return requests.get(f'https://therealrealdev.jamfcloud.com/JSSResource{url}',
#                         auth=HTTPBasicAuth(username, key), headers={'Accept': 'application/json'})


def computergroups() -> requests.models.Response:
    return trr_jamf('/computergroups')


def computergroup_by_id(computergroup_id: str) -> requests.models.Response:
    computer_group_url = f'/computergroups/id/{computergroup_id}'
    return trr_jamf(computer_group_url)


def computergroup_by_name(computergroup_name: str) -> requests.models.Response:
    computer_groups = computergroups().json()['computer_groups']
    for group in computer_groups:
        if group['name'] == computergroup_name:
            return computergroup_by_id(group['id'])


def computers() -> requests.models.Response:
    """'computers': [{'id': 225, 'name': 'NY65-M102770'}"""
    return trr_jamf('/computers')


def get_all_computers():
    # TODO make this async
    all_computers = []
    for comps in computers().json()['computers']:
        comp_id = comps['id']
        comp = computer_by_id(comp_id).json()
        all_computers.append(comp)

    return all_computers


def computer_by_id(computer_id: str) -> requests.models.Response:
    computer_url = f'/computers/id/{computer_id}'
    return trr_jamf(computer_url)


def computer_management(computer_management_id: str) -> requests.models.Response:
    computer_management_url = f'/computermanagement/id/{computer_management_id}'
    return trr_jamf(computer_management_url)


def directorybindings() -> requests.models.Response:
    return trr_jamf('/directorybindings')


def directorybinding(directorybinding_id: str) -> requests.models.Response:
    directorybinding_url = f"/directorybindings/id/{directorybinding_id}"
    return trr_jamf(directorybinding_url)


def directorybinding_by_name(name: str) -> requests.models.Response:
    directory_bindings = directorybindings().json()['directory_bindings']
    for bind in directory_bindings:
        if bind['name'] == name:
            return directorybinding(bind["id"])


def buildings() -> requests.models.Response:
    return trr_jamf('/buildings')


def policies() -> requests.models.Response:
    return trr_jamf('/policies')


def list_all_building_names():
    all_building_names = []
    building_s = buildings().json()['buildings']
    for building in building_s:
        all_building_names.append(building['name'])

    return all_building_names


def list_all_building_ids():
    all_building_names = []
    building_s = buildings().json()['buildings']
    for building in building_s:
        all_building_names.append(building['id'])

    return all_building_names


def list_all_policy_names():
    all_policie_names = []
    buildings = policies().json()['policies']
    for building in buildings:
        all_policie_names.append(building['name'])

    return all_policie_names


def list_all_smartgroup_names():
    all_smartgroup_names = []
    smartgroups = computergroups().json()['computer_groups']
    for smartgroup in smartgroups:
        all_smartgroup_names.append(smartgroup['name'])

    return all_smartgroup_names


def list_all_devices_past(hasnt_checked_in_since: int) -> list:
    list_past_checked_in_days = []
    for comps in computers().json()['computers']:
        comp_id = comps['id']
        comp = computer_by_id(comp_id).json()
        last_contact_time = comp['computer']['general']['last_contact_time']
        if not last_contact_time:
            pass
        elif last_contact_time == "":
            pass
        else:
            compare_dates = datetime.today() - datetime.strptime(last_contact_time.split(" ")[0], "%Y-%m-%d")
            if 'day' not in str(compare_dates):
                # less than 24 hours since check in
                pass
            else:
                days_since_last_checkin = int(str(compare_dates).split(" ")[0])
                if days_since_last_checkin >= hasnt_checked_in_since:
                    list_past_checked_in_days.append(comp)
                else:
                    pass

    return list_past_checked_in_days


def list_env_os_variants():
    """
    List all versions of OSX/macOS that exist in our jamf environment.
    """
    all_os_vers = set()
    for comp in get_all_computers():
        os_version = comp['computer']['hardware']['os_version']
        all_os_vers.add(os_version)

    return all_os_vers


list_env_os_variants()
