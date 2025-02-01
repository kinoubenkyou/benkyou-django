from selenium.webdriver.common.by import By

from main.tests.integration import DriverTestCase


class SignUserOutTestCase(DriverTestCase):
    def test(self) -> None:
        """Test success case."""
        self.web_driver.get(f"{self.live_server_url}/user/sign_out/")
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.assertEqual(
            self.web_driver.current_url, f"{self.live_server_url}/user/sign_in/"
        )
        client_session = self.web_driver.get_cookie("sessionid")
        self.assertIsNone(client_session)
