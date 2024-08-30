from main.tests.login_mixin import LoginMixin
from main.tests.test_case import TestCase


class UserSignInTestCase(LoginMixin, TestCase):
    def test_success(self):
        self.web_driver.get(f"{self.live_server_url}/user/sign_in/")
        self.login()

        self.assertEqual(len(self.find_elements("Signed in.")), 1)
