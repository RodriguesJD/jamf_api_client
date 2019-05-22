from oop_jamf.packages import Packages

item = Packages().get_trr_jamf()


def test_packages():

    assert item.status_code == 200


def test_packages_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Packages().by_name(test_name).status_code == 200


def test_packages_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Packages().by_id(test_id).status_code == 200


