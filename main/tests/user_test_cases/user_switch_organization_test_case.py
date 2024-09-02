from main.tests import TestCase
from main.tests.switch_organization_mixin import SwitchOrganizationMixin


class UserSwitchOrganizationTestCase(SwitchOrganizationMixin, TestCase):
    def test_success(self):
        self.web_driver.get(f"{self.live_server_url}/user/switch_organization/")
        self.sign_in()
        self.switch_organization()

        self.assertEqual(len(self.find_elements("Switched organization.")), 1)
