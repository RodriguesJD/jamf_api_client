from oop_jamf.categories import Categories

item = Categories().get_trr_jamf()


def test_categories():

    assert item.status_code == 200


def test_categories_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Categories().by_name(test_name).status_code == 200


def test_categories_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Categories().by_id(test_id).status_code == 200


