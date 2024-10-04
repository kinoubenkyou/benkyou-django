from main.tests.mixin import SignInMixin
from main.tests.test_case import TestCase


class UserReadTestCase(SignInMixin, TestCase):
    def test(self):
        self.web_driver.get(f"{self.live_server_url}/user/")
        self.sign_in()

        self.assertEqual(
            len(self.find_elements_with_text("Email: email1@email.com")),
            1,
        )
        self.assertEqual(len(self.find_elements_with_text("Email verified: False")), 1)
        self.assertEqual(len(self.find_elements_with_text("Name: name1")), 1)
