from django.test.testcases import LiveServerTestCase
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class DriverTestCase(LiveServerTestCase):
    def find_elements_contain_text(self, text):
        return [
            element
            for element in self.web_driver.find_elements(
                By.XPATH,
                f"//*[contains(text(), '{text}')]",
            )
            if element.is_displayed()
        ]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        cls.web_driver = WebDriver(options=options)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.web_driver.quit()
