from oop_jamf.licensedsoftware import Licensedsoftware

item = Licensedsoftware().get_trr_jamf()


def test_licensedsoftware():

    assert item.status_code == 200


def test_licensedsoftware_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Licensedsoftware().by_name(test_name).status_code == 200


def test_licensedsoftware_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Licensedsoftware().by_id(test_id).status_code == 200


