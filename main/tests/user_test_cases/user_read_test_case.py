from main.tests.login_mixin import LoginMixin
from main.tests.test_case import TestCase


class UserReadTestCase(LoginMixin, TestCase):
    def test_success(self):
        self.web_driver.get(f"{self.live_server_url}/user/")
        self.login()

        self.assertEqual(len(self.find_elements("Email: email@email.com")), 1)
        self.assertEqual(len(self.find_elements("Email verified: False")), 1)
        self.assertEqual(len(self.find_elements("Name: name")), 1)
