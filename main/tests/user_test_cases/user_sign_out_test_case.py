from selenium.webdriver.common.by import By

from main.tests.test_case import TestCase


class UserSignOutTestCase(TestCase):
    def test_success(self):
        self.web_driver.get(f"{self.live_server_url}/user/sign_out/")
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(len(self.find_elements("Signed out.")), 1)
