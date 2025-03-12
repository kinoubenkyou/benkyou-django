from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import url_changes

from main.models import User
from main.tests.integration import SeleniumTestCase


class CreateUserTestCase(SeleniumTestCase):
    def test(self) -> None:
        """Test success case."""
        url = f"{self.live_server_url}/user/create/"
        self.web_driver.get(url)
        username = "username1"
        self.find_input_and_replace_value("username", username)
        password = "Dr0wss@p1"
        self.find_input_and_replace_value("password1", password)
        self.find_input_and_replace_value("password2", password)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.web_driver_wait.until(url_changes(url))
        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}/user/sign_in/",
        )
        user = User.objects.filter(username=username).first()
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password(password))
