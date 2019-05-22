from oop_jamf.advancedcomputersearches import Advancedcomputersearches

item = Advancedcomputersearches().get_trr_jamf()


def test_advancedcomputersearches():

    assert item.status_code == 200


def test_advancedcomputersearches_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Advancedcomputersearches().by_name(test_name).status_code == 200


def test_advancedcomputersearches_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Advancedcomputersearches().by_id(test_id).status_code == 200


