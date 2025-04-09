from django.core import mail
from django.core.cache import cache
from django.utils.http import urlencode
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import url_changes

from main.test_cases.integration.live_server import LiveServerTestCase
from main.test_cases.integration.live_server.authentication_required_mixin import (
    AuthenticationRequiredMixin,
)


class StartVerifyUserEmailLiveServerTestCase(
    AuthenticationRequiredMixin, LiveServerTestCase
):
    fixtures = ["session", "user"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        self._test_authentication_required("user/start_verify_email/")

    def test(self) -> None:
        """Test success case."""
        self.add_session_cookie()
        url = f"{self.live_server_url}/user/start_verify_email/"
        self.web_driver.get(url)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.web_driver_wait.until(url_changes(url))
        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
        sentinel = object()
        token = cache.get("verify_user_email.1", sentinel)
        self.assertIsNot(token, sentinel)
        self.assertEqual(
            f"{self.live_server_url}/user/verify_email?{urlencode({'token': token})}",
            mail.outbox[0].body,
        )
        self.assertEqual(mail.outbox[0].subject, "Verify Email")
        self.assertIn("email1@email.com", mail.outbox[0].to)
