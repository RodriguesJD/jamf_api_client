from oop_jamf.usergroups import Usergroups

item = Usergroups().get_trr_jamf()


def test_usergroups():

    assert item.status_code == 200


def test_usergroups_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Usergroups().by_name(test_name).status_code == 200


def test_usergroups_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Usergroups().by_id(test_id).status_code == 200


