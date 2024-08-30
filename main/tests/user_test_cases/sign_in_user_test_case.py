from main.tests.login_mixin import LoginMixin
from main.tests.test_case import TestCase


class SignInUserTestCase(LoginMixin, TestCase):
    def test_success(self):
        self.login()

        self.assertEqual(
            self.web_driver.current_url, f"{self.live_server_url}/sign_in/done/"
        )
