from django.contrib.sessions.models import Session
from selenium.webdriver.common.by import By

from main.tests.integration import DriverTestCase


class SignUserInTestCase(DriverTestCase):
    fixtures = ["user"]  # type: ignore[assignment]

    def test(self) -> None:
        """Test success case."""
        self.web_driver.get(f"{self.live_server_url}/user/sign_in/")
        self.web_driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(
            "username1",
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(
            "Dr0wss@p1",
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
        server_session = Session.objects.first()
        client_session = self.web_driver.get_cookie("sessionid")
        self.assertIsNotNone(client_session)
        self.assertEqual(server_session.pk, client_session["value"])  # type: ignore[index]
        self.assertEqual(server_session.get_decoded()["_auth_user_id"], "1")
