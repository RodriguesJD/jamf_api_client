from oop_jamf.osxconfigurationprofiles import Osxconfigurationprofiles

item = Osxconfigurationprofiles().get_trr_jamf()


def test_osxconfigurationprofiles():

    assert item.status_code == 200


def test_osxconfigurationprofiles_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Osxconfigurationprofiles().by_name(test_name).status_code == 200


def test_osxconfigurationprofiles_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Osxconfigurationprofiles().by_id(test_id).status_code == 200


