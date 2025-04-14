from main.test_cases.integration.live_server import LiveServerTestCase
from main.test_cases.integration.live_server.authentication_required_mixin import (
    AuthenticationRequiredMixin,
)


class ReadUserLiveServerTestCase(AuthenticationRequiredMixin, LiveServerTestCase):
    fixtures = ["session", "user"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        self._test_authentication_required("user/")

    def test(self) -> None:
        """Test success case."""
        self.add_session_cookie()
        self.web_driver.get(f"{self.live_server_url}/user/")
        self.assertEqual(
            len(self.find_displayed_elements("last_login: Jan. 1, 2000, midnight")), 1
        )
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
        self.assertEqual(
            len(self.find_displayed_elements("email_is_verified: False")),
            1,
        )
