from main.tests.integration import DriverTestCase, SignInMixin


class SignUserInTestCase(SignInMixin, DriverTestCase):
    fixtures = ["sign_user_in"]  # type: ignore[assignment]

    def test(self) -> None:
        """Test success case."""
        self.web_driver.get(f"{self.live_server_url}/user/sign_in/")
        self.sign_in()
        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
