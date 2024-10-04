from main.tests.mixin import SwitchOrganizationMixin
from main.tests.test_case import TestCase


class OrganizationReadTestCase(SwitchOrganizationMixin, TestCase):
    def test(self):
        self.web_driver.get(f"{self.live_server_url}/organization/")
        self.sign_in()
        self.switch_organization()

        self.assertEqual(len(self.find_elements_with_text("Code: code1")), 1)
        self.assertEqual(len(self.find_elements_with_text("Name: name1")), 1)
