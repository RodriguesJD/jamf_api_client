from pprint import pprint

from core import get_trr_jamf


class UsersAdminRights:

    user_rights_per_station = []

    station_with_admin_rights = []
    station_without_admin_rights = []

    def users_with_admin_rights(self, station):
        # hostname = station[0]
        admin_station = []
        sn = station[1]
        for user in station[2]:
            # username = user[0]
            admin_rights = user[1]
            if admin_rights:

                admin_station = True
            else:
                pass

            if admin_station:
                self.station_with_admin_rights.append(sn)
            else:
                self.station_without_admin_rights.append(sn)

    def computers(self):
        for comp in get_trr_jamf.computers().json()['computers']:
            station = []
            comp_id = comp['id']
            computer = get_trr_jamf.computer_by_id(comp_id).json()['computer']
            hostname = computer['general']['name']
            station.append(hostname)
            serial_number = computer['general']['serial_number']
            station.append(serial_number)

            users_per_station = []
            local_accounts = computer['groups_accounts']['local_accounts']
            for user in local_accounts:
                username = user['name']
                if username == 'localadmin':
                    pass
                else:
                    adminrights = user['administrator']
                    users_per_station.append([username, adminrights])

            station.append(users_per_station)
            self.user_rights_per_station.append(station)
            self.users_with_admin_rights(station)

    def main(self):
        self.computers()
        print(f"stations with admin rights is {len(self.station_with_admin_rights)}")
        print(f"stations without admin rights is {len(self.station_without_admin_rights)}")


UsersAdminRights().main()
