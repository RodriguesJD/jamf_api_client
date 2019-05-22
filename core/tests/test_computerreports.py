from oop_jamf.computerreports import Computerreports

item = Computerreports().get_trr_jamf()


def test_computerreports():

    assert item.status_code == 200


def test_computerreports_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Computerreports().by_name(test_name).status_code == 200


def test_computerreports_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Computerreports().by_id(test_id).status_code == 200


