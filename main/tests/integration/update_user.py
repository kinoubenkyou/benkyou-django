from selenium.webdriver.common.by import By

from main.models import User
from main.tests.integration import AuthenticationRequiredMixin, DriverTestCase


class UpdateUserTestCase(AuthenticationRequiredMixin, DriverTestCase):
    fixtures = ["user"]  # type: ignore[assignment]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        self._test_authentication_required("user/update/")

    def test(self) -> None:
        """Test success case."""
        self.add_session_cookie()
        self.web_driver.get(f"{self.live_server_url}/user/update/")
        username = "username01"
        self.find_input_and_replace_value("username", username)
        last_name = "last_name01"
        self.find_input_and_replace_value("last_name", last_name)
        first_name = "first_name01"
        self.find_input_and_replace_value("first_name", first_name)
        email = "email01@email.com"
        self.find_input_and_replace_value("email", email)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
        self.assertEqual(
            User.objects.filter(
                username=username,
                last_name=last_name,
                first_name=first_name,
                email=email,
            ).count(),
            1,
        )
