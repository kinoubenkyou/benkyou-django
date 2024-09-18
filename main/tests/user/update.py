from selenium.webdriver.common.by import By

from main.tests.mixin import SignInMixin
from main.tests.test_case import TestCase


class UserUpdateTestCase(SignInMixin, TestCase):
    def test_success(self):
        name = "name"

        self.web_driver.get(f"{self.live_server_url}/user/update/")
        self.sign_in()
        self.web_driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(name)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
