from oop_jamf.ldapservers import Ldapservers

item = Ldapservers().get_trr_jamf()


def test_ldapservers():

    assert item.status_code == 200


def test_ldapservers_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Ldapservers().by_name(test_name).status_code == 200


def test_ldapservers_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Ldapservers().by_id(test_id).status_code == 200


