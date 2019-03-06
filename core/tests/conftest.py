import pytest
import time

from core import delete_trr_jamf
from core import get_trr_jamf

test_group_name = "testing_smart_group_api"

@pytest.fixture()
def before_computer_group_fixture():
    # TODO add test configuration file for test_group_name var
    computer_groups = get_trr_jamf.list_all_group_names()
    for group in computer_groups:
        if group == test_group_name:
            group_id = get_trr_jamf.computergroup_by_name(computergroup_name=test_group_name
                                                          ).json()['computer_group']['id']
            delete_trr_jamf.delete_computer_group(group_id=group_id)
            time.sleep(30)

    yield


@pytest.fixture()
def after_computer_group_fixture():

    yield

    computer_groups = get_trr_jamf.list_all_group_names()
    for group in computer_groups:
        if group == test_group_name:
            group_id = get_trr_jamf.computergroup_by_name(computergroup_name=test_group_name
                                                          ).json()['computer_group']['id']
            delete_trr_jamf.delete_computer_group(group_id=group_id)

    # TODO add an extra check for testing_smart_group_api group