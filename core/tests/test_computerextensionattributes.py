from oop_jamf.computerextensionattributes import Computerextensionattributes

item = Computerextensionattributes().get_trr_jamf()


def test_computerextensionattributes():

    assert item.status_code == 200


def test_computerextensionattributes_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Computerextensionattributes().by_name(test_name).status_code == 200


def test_computerextensionattributes_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Computerextensionattributes().by_id(test_id).status_code == 200


