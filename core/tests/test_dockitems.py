from oop_jamf.dockitems import Dockitems

item = Dockitems().get_trr_jamf()


def test_dockitems():

    assert item.status_code == 200


def test_dockitems_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Dockitems().by_name(test_name).status_code == 200


def test_dockitems_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Dockitems().by_id(test_id).status_code == 200


