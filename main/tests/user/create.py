from secrets import token_hex

from django.core import mail
from selenium.webdriver.common.by import By

from main.tests.test_case import TestCase


class UserCreateTestCase(TestCase):
    def test(self):
        email = "email@email.com"
        name = "name"
        password = token_hex()

        self.web_driver.get(f"{self.live_server_url}/user/create/")
        self.web_driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(
            email,
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(name)
        self.web_driver.find_element(By.XPATH, '//input[@name="password1"]').send_keys(
            password,
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password2"]').send_keys(
            password,
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
        self.assertIn(
            f"{self.live_server_url}/user/verify_email?token=",
            mail.outbox[0].body,
        )
        self.assertEqual(mail.outbox[0].subject, "Verify Email")
        self.assertIn("email@email.com", mail.outbox[0].to)
