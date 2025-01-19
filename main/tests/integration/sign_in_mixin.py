from selenium.webdriver.common.by import By

from main.tests.integration import DriverTestCase


class SignInMixin(DriverTestCase):
    def sign_in(self):
        self.web_driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(
            "username1",
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(
            "Dr0wss@p1",
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
