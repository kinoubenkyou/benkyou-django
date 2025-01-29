from typing import List

from django.test.testcases import LiveServerTestCase
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class DriverTestCase(LiveServerTestCase):
    web_driver: WebDriver

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

    @classmethod
    def setUpClass(cls) -> None:
        """Set up a web driver."""
        super().setUpClass()  # type: ignore[no-untyped-call]
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        cls.web_driver = WebDriver(options=options)

    @classmethod
    def tearDownClass(cls) -> None:
        """Quit the web driver."""
        super().tearDownClass()
        cls.web_driver.quit()
