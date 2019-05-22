from oop_jamf.computergroups import Computergroups

item = Computergroups().get_trr_jamf()


def test_computergroups():

    assert item.status_code == 200


def test_computergroups_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Computergroups().by_name(test_name).status_code == 200


def test_computergroups_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Computergroups().by_id(test_id).status_code == 200


