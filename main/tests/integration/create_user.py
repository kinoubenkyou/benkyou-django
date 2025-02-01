from selenium.webdriver.common.by import By

from main.models import User
from main.tests.integration import DriverTestCase


class CreateUserTestCase(DriverTestCase):
    def test(self) -> None:
        """Test success case."""
        self.web_driver.get(f"{self.live_server_url}/user/create/")
        username = "username1"
        self.find_input_and_replace_value("username", username)
        password = "Dr0wss@p1"
        self.find_input_and_replace_value("password1", password)
        self.find_input_and_replace_value("password2", password)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}/user/sign_in/",
        )
        user = User.objects.first()
        self.assertIsNotNone(user)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
