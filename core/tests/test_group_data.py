from jamf_analyzation.group_data.is_group_being_used import IsGroupBeingUsed


def test_search_for_group_data():
    """
    This checks a known group name and confirms search works. If it fails confirm that the group name still excists.
    :return:
    """
    assert isinstance(IsGroupBeingUsed("10.10 Yosemite").search_for_group_data().json(), dict)
    assert isinstance(IsGroupBeingUsed("86").search_for_group_data().json(), dict)
    assert isinstance(IsGroupBeingUsed(86).search_for_group_data().json(), dict)
    assert not IsGroupBeingUsed("bullshit").search_for_group_data()


# GroupAnalyzation().main()  # fail
# GroupAnalyzation(10000).main() # fail
# GroupAnalyzation('10000').main() # fail