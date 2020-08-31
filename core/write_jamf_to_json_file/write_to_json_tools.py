import os
import datetime


def data_needs_updating(base_file_name):
    filename = []
    for file in os.listdir(os.getcwd()):
        if base_file_name in file:
            filename.append(file)

    if len(filename) > 1:
        raise Exception(f"You have more than one {base_file_name}*.json.\n Please delete all of them except "
                        f"the one you wish to use. You can also delete all of them.")
    elif len(filename) == 0:
        return True, f"unused string"

    else:
        time_stamp = filename[0].split(base_file_name)[1].split(".json")[0].split("_")
        year = time_stamp[0]
        month = time_stamp[1]
        day = time_stamp[2]

        time_object = datetime.datetime(int(year), int(month), int(day))
        time_between_updates = (datetime.datetime.now() - time_object).days

        if time_between_updates >= 1:
            return True, "needs updating"
        else:
            return False, filename
