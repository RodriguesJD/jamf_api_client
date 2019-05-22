from oop_jamf.restrictedsoftware import Restrictedsoftware

item = Restrictedsoftware().get_trr_jamf()


def test_restrictedsoftware():

    assert item.status_code == 200


def test_restrictedsoftware_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Restrictedsoftware().by_name(test_name).status_code == 200


def test_restrictedsoftware_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Restrictedsoftware().by_id(test_id).status_code == 200


