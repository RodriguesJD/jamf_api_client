from oop_jamf.printers import Printers

item = Printers().get_trr_jamf()


def test_printers():

    assert item.status_code == 200


def test_printers_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Printers().by_name(test_name).status_code == 200


def test_printers_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Printers().by_id(test_id).status_code == 200


