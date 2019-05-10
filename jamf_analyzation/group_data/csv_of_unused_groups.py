import csv

from core import get_trr_jamf
from jamf_analyzation.group_data.is_group_being_used import IsGroupBeingUsed


class CsvUnusedGroups:
    """
    This class gets all unused groups by using the IsGroupBeingUsed class. If IsGroupBeingUsed returns false then the
    group is not being used. This class adds all unused groups to a list then writes that list to a csv file.
    """
    unused_groups = []

    def write_to_csv(self):
        with open('unused_groups.csv', mode='w') as unsued_group_file:
            employee_writer = csv.writer(unsued_group_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for unused_group in self.unused_groups:
                employee_writer.writerow([unused_group])

    def main(self):
        for group in get_trr_jamf.list_all_group_names():
            if IsGroupBeingUsed(group).main():
                self.unused_groups.append(group)
            else:
                pass

        self.write_to_csv()

        return 'Done'


if __name__ == '__main__':
    CsvUnusedGroups().main()