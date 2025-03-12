from django.test.testcases import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import url_changes
from selenium.webdriver.support.wait import WebDriverWait


class AuthenticationRequiredMixin(LiveServerTestCase):
    web_driver: WebDriver
    web_driver_wait: WebDriverWait[WebDriver]

    def _test_authentication_required(self, path: str) -> None:
        url = f"{self.live_server_url}/{path}"
        self.web_driver.get(url)
        self.web_driver_wait.until(url_changes(url))
        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}/user/sign_in/?next=/{path}",
        )
