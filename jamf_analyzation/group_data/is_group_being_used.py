from pprint import pprint

from core import get_trr_jamf


class IsGroupBeingUsed:
    """
    This is for gathering data on groups
    """
    def __init__(self, group_tag):
        self.group_tag = group_tag  # str or int

    def search_for_group_data(self):
        """
        Search for group using name or id. The id can be passed as a str or int.

        Returns
        -------
        group_data
            object "<class 'requests.models.Response'>"
        """
        if type(self.group_tag) == str:
            try:
                int(self.group_tag)  # this is for ints  that got passed as a stings
                group_data = get_trr_jamf.computergroup_by_id(int(self.group_tag))
            except ValueError:
                group_data = get_trr_jamf.computergroup_by_name(self.group_tag)
        elif type(self.group_tag) == int:
            group_data = get_trr_jamf.computergroup_by_id(self.group_tag)
        else:
            group_data = None

        return group_data

    def used_by_a_conf_policy(self) -> bool:
        """
        If used by other a configuration policy return True else return False

        Returns
        -------
            bool
        """
        used_by_policy = False
        all_conf_policies = get_trr_jamf.osxconfigurationprofiles().json()['os_x_configuration_profiles']
        for policy in all_conf_policies:
            policy_id = policy['id']
            policy_data = get_trr_jamf.osxconfigurationprofiles_by_id(policy_id).json()
            computer_groups_in_policy = policy_data['os_x_configuration_profile']['scope']['computer_groups']
            for computer_group in computer_groups_in_policy:
                group_in_policy = computer_group['name']
                if group_in_policy == self.group_tag:
                    used_by_policy = True

        return used_by_policy

    def used_by_a_policy(self) -> bool:
        """
        If used by other a policy return True else return False

        Returns
        -------
            bool
        """
        used_by_policy = False
        all_policies = get_trr_jamf.policies().json()['policies']
        for policy in all_policies:
            policy_id = policy['id']
            policy_data = get_trr_jamf.policy_by_id(policy_id).json()
            computer_groups_in_policy = policy_data['policy']['scope']['computer_groups']
            for computer_group in computer_groups_in_policy:
                group_in_policy = computer_group['name']
                if group_in_policy == self.group_tag:
                    used_by_policy = True

        return used_by_policy

    def used_by_other_smartgroup(self) -> bool:
        """
        If used by other smart group return True else return False

        Returns
        -------
            bool
        """
        used_by_smart_group = False
        all_groups = get_trr_jamf.list_all_group_names()
        for group in all_groups:
            group_data = get_trr_jamf.computergroup_by_name(group).json()
            group_criteria = group_data['computer_group']['criteria']
            for criteria in group_criteria:
                criteria_name = criteria['name']
                if criteria_name == 'Computer Group':
                    if criteria['value'] == self.group_tag:
                        used_by_smart_group = True  # if group is found in criteria['value'] then it is being used

        return used_by_smart_group

    def main(self):
        if not self.search_for_group_data():
            raise Exception(f"No jamf group found using '{self.group_tag}' as the search criteria.")
        else:
            if self.used_by_other_smartgroup() or self.used_by_a_policy() or self.used_by_a_conf_policy():
                is_group_used = True
            else:
                is_group_used = False

        return is_group_used
