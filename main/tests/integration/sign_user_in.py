from selenium.webdriver.common.by import By

from main.tests.integration import DriverTestCase


class SignUserInTestCase(DriverTestCase):
    fixtures = ["sign_user_in"]  # type: ignore[assignment]

    def test(self):
        self.web_driver.get(f"{self.live_server_url}/user/sign_in/")
        self.web_driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(
            "username1",
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(
            "Dr0wss@p1",
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
