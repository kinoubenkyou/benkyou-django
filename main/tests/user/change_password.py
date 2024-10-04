from secrets import token_hex

from selenium.webdriver.common.by import By

from main.tests.mixin import SignInMixin
from main.tests.test_case import TestCase


class UserChangePasswordTestCase(SignInMixin, TestCase):
    def test(self):
        password = token_hex()

        self.web_driver.get(f"{self.live_server_url}/user/change_password/")
        self.sign_in()
        self.web_driver.find_element(
            By.XPATH,
            '//input[@name="old_password"]',
        ).send_keys("dr0wss@p1")
        self.web_driver.find_element(
            By.XPATH,
            '//input[@name="new_password1"]',
        ).send_keys(password)
        self.web_driver.find_element(
            By.XPATH,
            '//input[@name="new_password2"]',
        ).send_keys(password)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
