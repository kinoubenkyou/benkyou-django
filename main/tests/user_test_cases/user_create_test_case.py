from django.core import mail
from selenium.webdriver.common.by import By

from main.tests import TestCase


class UserCreateTestCase(TestCase):
    def test_success(self):
        email = "email@email.com"
        password = "dr0wss@p"

        self.web_driver.get(f"{self.live_server_url}/user/create/")
        self.web_driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(
            email
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(
            "name"
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password1"]').send_keys(
            password
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password2"]').send_keys(
            password
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(len(self.find_elements("Created user.")), 1)
        self.assertIn(
            f"{self.live_server_url}/user/verify_email/?token=", mail.outbox[0].body
        )
        self.assertEqual(mail.outbox[0].subject, "Verify Email")
        self.assertIn(email, mail.outbox[0].to)
