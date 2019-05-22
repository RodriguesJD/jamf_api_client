from oop_jamf.buildings import Buildings

item = Buildings().get_trr_jamf()


def test_buildings():

    assert item.status_code == 200


def test_buildings_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Buildings().by_name(test_name).status_code == 200


def test_buildings_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Buildings().by_id(test_id).status_code == 200


