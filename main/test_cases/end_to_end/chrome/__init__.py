from typing import List

from django.core.cache import cache
from django.test.testcases import LiveServerTestCase
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class ChromeTestCase(LiveServerTestCase):
    def add_session_cookie(self) -> None:
        """Add session cookie."""
        self.web_driver.get(f"{self.live_server_url}/")
        self.web_driver.add_cookie(
            {
                "name": "sessionid",
                "value": "544vzd71puvnac7vyzermrtwjkwuq55w",
            }
        )

    def find_displayed_elements(self, text: str) -> List[WebElement]:
        """Find displayed elements by text."""
        return [
            element
            for element in self.web_driver.find_elements(
                By.XPATH,
                f"//*[contains(text(), '{text}')]",
            )
            if element.is_displayed()
        ]

    def find_input_and_replace_value(self, input_name: str, value: str) -> None:
        """Find an input by name attribute and replace the value property."""
        user_input = self.web_driver.find_element(
            By.XPATH, f'//input[@name="{input_name}"]'
        )
        user_input.clear()
        user_input.send_keys(value)

    def setUp(self) -> None:
        """Set up a web driver."""
        super().setUp()
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.timeouts = {"implicit": 1000, "pageLoad": 1000}
        self.web_driver = WebDriver(options=options)
        self.web_driver_wait = WebDriverWait(self.web_driver, 1)

    def tearDown(self) -> None:
        """Clear cache, quit the web driver."""
        cache.clear()
        self.web_driver.quit()
        super().tearDown()
