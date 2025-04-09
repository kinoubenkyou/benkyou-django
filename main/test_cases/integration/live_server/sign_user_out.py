from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import url_changes

from main.test_cases.integration.live_server import LiveServerTestCase


class SignUserOutLiveServerTestCase(LiveServerTestCase):
    def test(self) -> None:
        """Test success case."""
        url = f"{self.live_server_url}/user/sign_out/"
        self.web_driver.get(url)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.web_driver_wait.until(url_changes(url))
        self.assertEqual(
            self.web_driver.current_url, f"{self.live_server_url}/user/sign_in/"
        )
        client_session = self.web_driver.get_cookie("sessionid")
        self.assertIsNone(client_session)
