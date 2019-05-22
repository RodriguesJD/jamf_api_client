from oop_jamf.mobiledevicegroups import Mobiledevicegroups

item = Mobiledevicegroups().get_trr_jamf()


def test_mobiledevicegroups():

    assert item.status_code == 200


def test_mobiledevicegroups_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Mobiledevicegroups().by_name(test_name).status_code == 200


def test_mobiledevicegroups_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Mobiledevicegroups().by_id(test_id).status_code == 200


