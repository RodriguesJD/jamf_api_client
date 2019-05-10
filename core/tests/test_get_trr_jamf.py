from core import get_trr_jamf
# https://developer.jamf.com/apis/jamf-pro-api/index


def test_trr_jamf():
    assert get_trr_jamf.get_trr_jamf('/computergroups').status_code == 200
    assert get_trr_jamf.get_trr_jamf('not_a_url').status_code == 404
    assert isinstance(get_trr_jamf.get_trr_jamf('/sites').json(), dict)
    assert str(type(get_trr_jamf.get_trr_jamf('/sites'))) == "<class 'requests.models.Response'>"


def test_computergroups():
    assert get_trr_jamf.computergroups().status_code == 200
    assert get_trr_jamf.get_trr_jamf('/computergroups').status_code == 200
    assert isinstance(get_trr_jamf.computergroups().json(), dict)
    assert str(type(get_trr_jamf.computergroups())) == "<class 'requests.models.Response'>"


def test_computergroup():
    assert get_trr_jamf.get_trr_jamf('/computergroups/id/95').status_code == 200
    assert get_trr_jamf.computergroup_by_id(95).status_code == 200
    assert isinstance(get_trr_jamf.computergroup_by_id(95).json(), dict)
    assert str(type(get_trr_jamf.computergroup_by_id(95
                                                     ))) == "<class 'requests.models.Response'>"


def test_computergroup_by_name():
    assert get_trr_jamf.computergroup_by_name("ESET AV missing")
    assert get_trr_jamf.computergroup_by_name("ESET AV missing").status_code == 200
    assert isinstance(get_trr_jamf.computergroup_by_name("ESET AV missing").json(), dict)
    assert get_trr_jamf.computergroup_by_name("wrong group name") is None
    assert str(type(get_trr_jamf.computergroup_by_name("ESET AV missing"))) == "<class 'requests.models.Response'>"


def test_computers():
    assert get_trr_jamf.computers().status_code == 200
    assert isinstance(get_trr_jamf.get_trr_jamf('/computers').json(), dict)
    assert str(type(get_trr_jamf.get_trr_jamf('/computers'))) == "<class 'requests.models.Response'>"


def test_get_all_computers():
    assert isinstance(get_trr_jamf.get_all_computers(), list)
    for computer in get_trr_jamf.get_all_computers():
        assert isinstance(computer, dict)


def test_computer():
    assert get_trr_jamf.computer_by_id(20).status_code == 200
    assert get_trr_jamf.computer_by_id("not an int").status_code == 404
    assert isinstance(get_trr_jamf.computer_by_id(20).json(), dict)
    assert str(type(get_trr_jamf.computer_by_id(20))) == "<class 'requests.models.Response'>"


def test_computer_management():
    assert get_trr_jamf.get_trr_jamf('/computermanagement/id/20').status_code == 200
    assert get_trr_jamf.get_trr_jamf('not a url string').status_code == 404
    assert isinstance(get_trr_jamf.computer_management(20).json(), dict)
    assert str(type(get_trr_jamf.computer_management(20))) == "<class 'requests.models.Response'>"


def test_directorybindings():
    assert get_trr_jamf.get_trr_jamf('/directorybindings').status_code == 200
    assert get_trr_jamf.directorybindings().status_code == 200
    assert isinstance(get_trr_jamf.directorybindings().json(), dict)
    assert str(type(get_trr_jamf.directorybindings())) == "<class 'requests.models.Response'>"


def test_directorybinding():
    assert get_trr_jamf.get_trr_jamf('/directorybindings/id/10').status_code == 200
    assert get_trr_jamf.directorybinding(10).status_code == 200
    assert get_trr_jamf.directorybinding('not an int').status_code == 404
    assert isinstance(get_trr_jamf.directorybinding(10).json(), dict)
    assert str(type(get_trr_jamf.directorybinding(10))) == "<class 'requests.models.Response'>"


def test_directorybinding_by_name():
    trr_buildings = get_trr_jamf.buildings().json()["buildings"]
    for site in trr_buildings:
        builing_bind = f"{site['name']} Directory Binding"
        if builing_bind =='Remote Directory Binding':
            pass
        else:
            assert get_trr_jamf.directorybinding_by_name(builing_bind)
            assert get_trr_jamf.directorybinding_by_name(builing_bind).status_code == 200
            assert isinstance(get_trr_jamf.directorybinding_by_name(builing_bind).json(), dict)
            assert str(type(get_trr_jamf.directorybinding_by_name(builing_bind))) == "<class 'requests.models.Response'>"
            assert get_trr_jamf.directorybinding_by_name("not a site name") is None


def test_buildings():
    assert get_trr_jamf.buildings().status_code == 200
    assert isinstance(get_trr_jamf.get_trr_jamf('/buildings').json(), dict)
    assert str(type(get_trr_jamf.get_trr_jamf('/buildings'))) == "<class 'requests.models.Response'>"


def test_policies():
    assert get_trr_jamf.policies().status_code == 200
    assert isinstance(get_trr_jamf.get_trr_jamf('/policies').json(), dict)
    assert str(type(get_trr_jamf.get_trr_jamf('/policies'))) == "<class 'requests.models.Response'>"


def test_policy_by_id():
    assert get_trr_jamf.policy_by_id(120).status_code == 200
    assert isinstance(get_trr_jamf.get_trr_jamf('/policies/id/120').json(), dict)
    assert str(type(get_trr_jamf.policy_by_id(120))) == "<class 'requests.models.Response'>"


def test_list_all_policy_names():
    assert isinstance(get_trr_jamf.list_all_policy_names(), list)
    for policy_name in get_trr_jamf.list_all_policy_names():
        assert isinstance(policy_name, str)


def test_list_all_building_names():
    assert isinstance(get_trr_jamf.list_all_building_names(), list)
    for building_name in get_trr_jamf.list_all_building_names():
        assert isinstance(building_name, str)


def test_list_all_building_ids():
    assert isinstance(get_trr_jamf.list_all_building_ids(), list)
    for building_id in get_trr_jamf.list_all_building_ids():
        assert isinstance(building_id, int)


def test_list_all_smartgroup_names():
    assert isinstance(get_trr_jamf.list_all_smartgroup_names(), list)
    for smartgroup in get_trr_jamf.list_all_smartgroup_names():
        assert isinstance(smartgroup, str)
        # TODO test that its smart


def test_list_all_staticgroup_names():
    assert isinstance(get_trr_jamf.list_all_staticgroup_names(), list)
    for staticgroup in get_trr_jamf.list_all_staticgroup_names():
        assert isinstance(staticgroup, str)
        # TODO test that its static


def test_list_all_group_names():
    assert isinstance(get_trr_jamf.list_all_group_names(), list)
    for group in get_trr_jamf.list_all_group_names():
        assert isinstance(group, str)


def test_list_all_devices_past():
    assert isinstance(get_trr_jamf.list_all_devices_past(5), list)


def test_list_env_os_variants():
    assert isinstance(get_trr_jamf.list_env_os_variants(), set)

