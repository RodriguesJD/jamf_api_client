from jamf_analyzation.retouching.retouching import RetouchingAnalyzation


class TestRetouchingAnalyzation:

    retouch = RetouchingAnalyzation()


    def test_parse_applications(self):
        retouching_staticgroup = self.retouch.retouching_static_group().json()
        computer_data = self.retouch.computers_in_group(retouching_staticgroup)
        for computer in computer_data:
            applications = computer['computer']['software']['applications']
            parsed_app_data = self.retouch.parse_applications(applications)
            assert isinstance(parsed_app_data, list)
            assert len(parsed_app_data) == 16

    def test_parse_computer_data(self):
        retouching_staticgroup = self.retouch.retouching_static_group().json()
        computer_data = self.retouch.computers_in_group(retouching_staticgroup)
        parsed_retouching = self.retouch.parse_computer_data(computer_data)

        assert isinstance(parsed_retouching, list)
        for parsed_computer in parsed_retouching:
            assert isinstance(parsed_computer, list)

    def test_computers_in_group(self):
        retouching_staticgroup = self.retouch.retouching_static_group().json()
        computer_data = self.retouch.computers_in_group(retouching_staticgroup)
        assert isinstance(computer_data, list)
        for computer in computer_data:
            assert isinstance(computer, dict)
            hostname = computer['computer']['general']['name']
            assert isinstance(hostname, str)
            serial_number = computer['computer']['general']['serial_number']
            assert isinstance(serial_number, str)

    def test_retouching_static_group(self):
        retouching_staticgroup = self.retouch.retouching_static_group()
        # confirm RetouchingAnalyzation().retouching_static_group is an object
        assert isinstance(retouching_staticgroup, object)
        assert str(type(retouching_staticgroup)) == "<class 'requests.models.Response'>"  # confirm its a request object
        assert isinstance(retouching_staticgroup.json(), dict)  # Confirm that json() converts it to a dict

