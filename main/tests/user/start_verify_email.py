from django.core import mail
from selenium.webdriver.common.by import By

from main.tests.mixin import SignInMixin
from main.tests.test_case import TestCase


class UserStartVerifyEmailTestCase(SignInMixin, TestCase):
    def test_success(self):
        self.web_driver.get(f"{self.live_server_url}/user/start_verify_email/")
        self.sign_in()

        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}/user/")
        self.assertIn(
            f"{self.live_server_url}/user/verify_email?token=",
            mail.outbox[0].body,
        )
        self.assertEqual(mail.outbox[0].subject, "Verify Email")
        self.assertIn("email1@email.com", mail.outbox[0].to)
