from main.tests.mixin import SwitchOrganizationMixin
from main.tests.test_case import TestCase


class OrganizationReadTestCase(SwitchOrganizationMixin, TestCase):
    def test_success(self):
        self.web_driver.get(f"{self.live_server_url}/organization/")
        self.sign_in()
        self.switch_organization()

        self.assertEqual(len(self.find_elements("Code: code")), 1)
        self.assertEqual(len(self.find_elements("Name: name")), 1)
