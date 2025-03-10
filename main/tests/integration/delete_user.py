from selenium.webdriver.common.by import By

from main.models import User
from main.tests.integration import AuthenticationRequiredMixin, SeleniumTestCase


class DeleteUserTestCase(AuthenticationRequiredMixin, SeleniumTestCase):
    fixtures = ["session", "user"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        self._test_authentication_required("user/delete/")

    def test(self) -> None:
        """Test success case."""
        self.add_session_cookie()
        self.web_driver.get(f"{self.live_server_url}/user/delete/")
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.assertEqual(
            self.web_driver.current_url, f"{self.live_server_url}/user/sign_in/"
        )
        self.assertFalse(User.objects.filter(pk=1).exists())
