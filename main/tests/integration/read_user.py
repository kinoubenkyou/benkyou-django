from main.tests.integration import SignedInTestCase


class ReadUserTestCase(SignedInTestCase):
    fixtures = ["read_user"]  # type: ignore[assignment]

    def test(self):
        self.web_driver.get(f"{self.live_server_url}/user/")
        self.assertEqual(
            len(self.find_elements_with_text("last_login: Jan. 1, 2000, midnight")), 1
        )
        self.assertEqual(len(self.find_elements_with_text("username: username1")), 1)
        self.assertEqual(
            len(self.find_elements_with_text("first_name: first_name1")), 1
        )
        self.assertEqual(len(self.find_elements_with_text("last_name: last_name1")), 1)
        self.assertEqual(
            len(self.find_elements_with_text("email: email1@email.com")), 1
        )
        self.assertEqual(
            len(self.find_elements_with_text("date_joined: Jan. 1, 2000, midnight")), 1
        )
