from selenium.webdriver.common.by import By

from main.tests.mixin import SwitchOrganizationMixin
from main.tests.test_case import TestCase


class OrganizationUpdateTestCase(SwitchOrganizationMixin, TestCase):
    def test(self):
        self.web_driver.get(f"{self.live_server_url}/organization/update/")
        self.sign_in()
        self.switch_organization()
        code_input = self.web_driver.find_element(By.XPATH, '//input[@name="code"]')
        code_input.clear()
        code_input.send_keys("code_")
        name_input = self.web_driver.find_element(By.XPATH, '//input[@name="name"]')
        name_input.clear()
        name_input.send_keys("name_")
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(len(self.find_elements_with_text("Code: code_")), 1)
        self.assertEqual(len(self.find_elements_with_text("Name: name_")), 1)
