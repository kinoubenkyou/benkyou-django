from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import url_changes

from main.models import User
from main.test_cases.end_to_end.chrome import ChromeTestCase
from main.test_cases.end_to_end.chrome.authentication_required_mixin import (
    AuthenticationRequiredMixin,
)


class DeleteUserTestCase(AuthenticationRequiredMixin, ChromeTestCase):
    fixtures = ["session", "user"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        self._test_authentication_required("user/delete/")

    def test(self) -> None:
        """Test success case."""
        self.add_session_cookie()
        url = f"{self.live_server_url}/user/delete/"
        self.web_driver.get(url)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.web_driver_wait.until(url_changes(url))
        self.assertEqual(
            self.web_driver.current_url, f"{self.live_server_url}/user/sign_in/"
        )
        self.assertFalse(User.objects.filter(pk=1).exists())
