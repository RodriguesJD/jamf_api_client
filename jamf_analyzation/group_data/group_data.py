from pprint import pprint

from core import get_trr_jamf


class GroupAnalyzation:
    """
    This is for gathering data on groups
    """
    def __init__(self, group_tag):
        self.group_tag = group_tag  # str or int

    def search_for_group_data(self):
        if type(self.group_tag) == str:
            try:
                int(self.group_tag)
                group_data = get_trr_jamf.computergroup_by_id(int(self.group_tag))
            except ValueError:
                group_data = get_trr_jamf.computergroup_by_name(self.group_tag)
        elif type(self.group_tag) == int:
            group_data = get_trr_jamf.computergroup_by_id(self.group_tag)
        else:
            group_data = None

        return group_data

    def is_smart(self):
        """
        return bool if smart true else false
        :return:
        """
        pass

    def main(self):
        if not self.search_for_group_data():
            raise Exception(f"No jamf group found using '{self.group_tag}' as the search criteria.")
        else:
            self.is_smart()
            print(self.search_for_group_data().json())
            # TODO check to see if any policy, configuration policy, or smart group is using this group.


GroupAnalyzation("10.10 Yosemite").main()