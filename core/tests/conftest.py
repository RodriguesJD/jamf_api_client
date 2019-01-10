import pytest
import time

from core import delete_trr_jamf
from core import get_trr_jamf


@pytest.fixture()
def computer_group_fixture():
    # TODO add test configuration file for test_group_name var
    test_group_name = "testing_smart_group_api"

    def is_group_name_in_groups():
        computer_group_names = []
        computer_groups = get_trr_jamf.list_all_smartgroup_names()
        for group in computer_groups:
            computer_group_names.append(group)

        if test_group_name in computer_group_names:
            in_groups = True
        else:
            in_groups = False

        return in_groups

    if is_group_name_in_groups():
        time.sleep(30)

    if is_group_name_in_groups():  # If its still there after 30 seconds then delete it
        try:
            group_id = get_trr_jamf.computergroup_by_name(computergroup_name=test_group_name).json()['computer_group']['id']
            delete_trr_jamf.delete_computer_group(group_id=group_id)
        except AttributeError:
            pass

    yield

    if not is_group_name_in_groups():
        time.sleep(30)  # Some times i run the tests faster than the api endpoint updated the api
        if not is_group_name_in_groups():
            time.sleep(60)
    else:
        try:
            group_id = get_trr_jamf.computergroup_by_name(computergroup_name=test_group_name).json()['computer_group']['id']
            delete_trr_jamf.delete_computer_group(group_id=group_id)
        except AttributeError:
            pass


