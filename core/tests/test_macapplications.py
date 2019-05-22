from oop_jamf.macapplications import Macapplications

item = Macapplications().get_trr_jamf()


def test_macapplications():

    assert item.status_code == 200


def test_macapplications_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Macapplications().by_name(test_name).status_code == 200


def test_macapplications_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Macapplications().by_id(test_id).status_code == 200


