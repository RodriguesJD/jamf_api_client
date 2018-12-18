from trr_jamf import trr_jamf
# https://developer.jamf.com/apis/jamf-pro-api/index


def test_trr_jamf():
    assert trr_jamf.trr_jamf('/computergroups').status_code == 200
    assert trr_jamf.trr_jamf('not_a_url').status_code == 404
    assert isinstance(trr_jamf.trr_jamf('/sites').json(), dict)
    assert str(type(trr_jamf.trr_jamf('/sites'))) == "<class 'requests.models.Response'>"


def test_computergroups():
    assert trr_jamf.computergroups().status_code == 200
    assert trr_jamf.trr_jamf('/computergroups').status_code == 200
    assert isinstance(trr_jamf.computergroups().json(), dict)
    assert str(type(trr_jamf.computergroups())) == "<class 'requests.models.Response'>"


def test_computergroup():
    assert trr_jamf.trr_jamf('/computergroups/id/12').status_code == 200
    assert trr_jamf.computergroup_by_id(12).status_code == 200
    assert isinstance(trr_jamf.computergroup_by_id(12).json(), dict)
    assert str(type(trr_jamf.computergroup_by_id(12))) == "<class 'requests.models.Response'>"


def test_computergroup_by_name():
    assert trr_jamf.computergroup_by_name("ESET AV missing")
    assert trr_jamf.computergroup_by_name("ESET AV missing").status_code == 200
    assert isinstance(trr_jamf.computergroup_by_name("ESET AV missing").json(), dict)
    assert trr_jamf.computergroup_by_name("wrong group name") is None
    assert str(type(trr_jamf.computergroup_by_name("ESET AV missing"))) == "<class 'requests.models.Response'>"


def test_computers():
    assert trr_jamf.computers().status_code == 200
    assert isinstance(trr_jamf.trr_jamf('/computers').json(), dict)
    assert str(type(trr_jamf.trr_jamf('/computers'))) == "<class 'requests.models.Response'>"


def test_computer():
    assert trr_jamf.computer_by_id(20).status_code == 200
    assert trr_jamf.computer_by_id("not an int").status_code == 404
    assert isinstance(trr_jamf.computer_by_id(20).json(), dict)
    assert str(type(trr_jamf.computer_by_id(20))) == "<class 'requests.models.Response'>"


def test_computer_management():
    assert trr_jamf.trr_jamf('/computermanagement/id/20').status_code == 200
    assert trr_jamf.trr_jamf('not a url string').status_code == 404
    assert isinstance(trr_jamf.computer_management(20).json(), dict)
    assert str(type(trr_jamf.computer_management(20))) == "<class 'requests.models.Response'>"


def test_directorybindings():
    assert trr_jamf.trr_jamf('/directorybindings').status_code == 200
    assert trr_jamf.directorybindings().status_code == 200
    assert isinstance(trr_jamf.directorybindings().json(), dict)
    assert str(type(trr_jamf.directorybindings())) == "<class 'requests.models.Response'>"


def test_directorybinding():
    assert trr_jamf.trr_jamf('/directorybindings/id/10').status_code == 200
    assert trr_jamf.directorybinding(10).status_code == 200
    assert trr_jamf.directorybinding('not an int').status_code == 404
    assert isinstance(trr_jamf.directorybinding(10).json(), dict)
    assert str(type(trr_jamf.directorybinding(10))) == "<class 'requests.models.Response'>"


def test_directorybinding_by_name():
    trr_buildings = trr_jamf.buildings().json()["buildings"]
    for site in trr_buildings:
        builing_bind = f"{site['name']} Directory Binding"
        if builing_bind =='Remote Directory Binding':
            pass
        else:
            assert trr_jamf.directorybinding_by_name(builing_bind)
            assert trr_jamf.directorybinding_by_name(builing_bind).status_code == 200
            assert isinstance(trr_jamf.directorybinding_by_name(builing_bind).json(), dict)
            assert str(type(trr_jamf.directorybinding_by_name(builing_bind))) == "<class 'requests.models.Response'>"
            assert trr_jamf.directorybinding_by_name("not a site name") is None


def test_buildings():
    assert trr_jamf.buildings().status_code == 200
    assert isinstance(trr_jamf.trr_jamf('/buildings').json(), dict)
    assert str(type(trr_jamf.trr_jamf('/buildings'))) == "<class 'requests.models.Response'>"


def test_policies():
    assert trr_jamf.policies().status_code == 200
    assert isinstance(trr_jamf.trr_jamf('/policies').json(), dict)
    assert str(type(trr_jamf.trr_jamf('/policies'))) == "<class 'requests.models.Response'>"


def test_list_all_building_names():
    assert isinstance(trr_jamf.list_all_building_names(), list)
    for building_name in trr_jamf.list_all_building_names():
        assert isinstance(building_name, str)

def test_list_all_building_ids():
    assert isinstance(trr_jamf.list_all_building_ids(), list)
    for building_id in trr_jamf.list_all_building_ids():
        assert isinstance(building_id, int)


def test_list_all_policy_names():
    assert isinstance(trr_jamf.list_all_policy_names(), list)
    for policy_name in trr_jamf.list_all_policy_names():
        assert isinstance(policy_name, str)


def test_list_all_smartgroup_names():
    assert isinstance(trr_jamf.list_all_smartgroup_names(), list)
    for policy_name in trr_jamf.list_all_smartgroup_names():
        assert isinstance(policy_name, str)


def test_list_all_devices_past():
    assert isinstance(trr_jamf.list_all_devices_past(5), list)


def test_checked_in_exceeds_date():
    #TODO need to figure out the logic so i dont have to hard code this one
    pass
