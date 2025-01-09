from django.test.testcases import LiveServerTestCase
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class IntegrationTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        cls.web_driver = WebDriver(options=options)

    def tearDown(self):
        super().tearDown()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.web_driver.quit()
