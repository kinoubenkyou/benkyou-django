from selenium.webdriver.common.by import By

from main.models import User
from main.tests.integration import DriverTestCase


class CreateUserTestCase(DriverTestCase):
    def test(self) -> None:
        self.web_driver.get(f"{self.live_server_url}/user/create/")
        username = "username1"
        self.clear_and_send_keys("username", username)
        password = "Dr0wss@p1"
        self.clear_and_send_keys("password1", password)
        self.clear_and_send_keys("password2", password)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}/user/sign_in/",
        )
        user = User.objects.filter(username=username).first()
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password(password))
