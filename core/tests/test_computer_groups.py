import pytest
import time
from core import get_trr_jamf
from core import post_trr_jamf
from core import put_trr_jamf
#  pytest core/tests/test_computer_groups.py


@pytest.mark.usefixtures('computer_group_fixture')
class TestComputerGroups:

    test_group_name = "testing_smart_group_api"
    host_id = '394'  # this is the host id of Jeremy Rodrigues
    group_id = []

    def is_group_name_in_groups(self):
        computer_group_names = []
        computer_groups = get_trr_jamf.list_all_smartgroup_names()
        for group in computer_groups:
            computer_group_names.append(group)

        if self.test_group_name in computer_group_names:
            in_groups = True
        else:
            in_groups = False

        return in_groups

    def test_create_computer_group(self):
        # assert not self.is_group_name_in_groups()
        create_group = post_trr_jamf.create_computer_group(new_group_name=self.test_group_name)
        created = 201
        assert create_group.status_code == created
        self.group_id.append(create_group.text.split('<id>')[1].split('</id>')[0])
        # TODO add while loop instead of hacky time.sleep
        time.sleep(45)

    def test_add_host_to_comp_group(self):
        add_host = put_trr_jamf.add_host_to_comp_group(group_id=self.group_id[0],
                                                       add_host_id=self.host_id,
                                                       group_name=self.test_group_name)
        assert add_host.status_code == 201
        assert isinstance(self.group_id[0], str)
        assert len(self.group_id[0]) == 3

    # TODO add delete test func 







