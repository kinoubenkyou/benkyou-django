from django.test.testcases import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


class AuthenticationRequiredMixin(LiveServerTestCase):
    web_driver: WebDriver

    def _test_authentication_required(self, path: str) -> None:
        self.web_driver.get(f"{self.live_server_url}/{path}")
        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}/user/sign_in/?next=/{path}",
        )
