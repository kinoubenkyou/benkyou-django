from main.tests.mixin import SignInMixin
from main.tests.test_case import TestCase


class UserSignInTestCase(SignInMixin, TestCase):
    def test_success(self):
        self.web_driver.get(f"{self.live_server_url}/user/sign_in/")
        self.sign_in()

        self.assertEqual(len(self.find_elements_with_text("Signed in.")), 1)
