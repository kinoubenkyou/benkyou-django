from main.tests.integration import SignInMixin, DriverTestCase


class ReadUserTestCase(SignInMixin, DriverTestCase):
    fixtures = ["read_user"]  # type: ignore[assignment]

    def test(self) -> None:
        """Test success case."""
        self.web_driver.get(f"{self.live_server_url}/user/")
        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}/user/sign_in/?next=/user/",
        )
        self.sign_in()
        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
        self.assertEqual(len(self.find_displayed_elements("last_login:")), 1)
        self.assertEqual(len(self.find_displayed_elements("username: username1")), 1)
        self.assertEqual(
            len(self.find_displayed_elements("first_name: first_name1")), 1
        )
        self.assertEqual(len(self.find_displayed_elements("last_name: last_name1")), 1)
        self.assertEqual(
            len(self.find_displayed_elements("email: email1@email.com")), 1
        )
        self.assertEqual(
            len(self.find_displayed_elements("date_joined: Jan. 1, 2000, midnight")),
            1,
        )
