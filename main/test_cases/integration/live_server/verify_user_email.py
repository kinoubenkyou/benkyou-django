from secrets import token_urlsafe

from django.core.cache import cache
from django.utils.http import urlencode
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import url_changes

from main.models import User
from main.test_cases.integration.live_server import LiveServerTestCase
from main.test_cases.integration.live_server.authentication_required_mixin import (
    AuthenticationRequiredMixin,
)


class VerifyUserEmailLiveServerTestCase(
    AuthenticationRequiredMixin, LiveServerTestCase
):
    fixtures = ["session", "user"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        self._test_authentication_required("user/verify_email/")

    def test(self) -> None:
        """Test success case."""
        self.add_session_cookie()
        token = token_urlsafe()
        cache.set("verify_user_email.1", token, 600)
        url = f"{self.live_server_url}/user/verify_email?{urlencode({'token': token})}"
        self.web_driver.get(url)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.web_driver_wait.until(url_changes(url))
        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
        self.assertTrue(User.objects.get(pk=1).email_is_verified)

    def test__incorrect_token(self) -> None:
        """Test success case."""
        self.add_session_cookie()
        token = token_urlsafe()
        cache.set("verify_user_email.1", token, 600)
        url = f"{self.live_server_url}/user/verify_email?{urlencode({'token': '_'})}"
        self.web_driver.get(url)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.assertEqual(len(self.find_displayed_elements("incorrect token")), 1)

    def test__token_not_found(self) -> None:
        """Test success case."""
        self.add_session_cookie()
        token = token_urlsafe()
        cache.set("verify_user_email.1", token, 0)
        url = f"{self.live_server_url}/user/verify_email?{urlencode({'token': token})}"
        self.web_driver.get(url)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.assertEqual(len(self.find_displayed_elements("token not found")), 1)
