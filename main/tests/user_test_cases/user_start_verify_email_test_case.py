from django.core import mail
from selenium.webdriver.common.by import By

from main.tests import TestCase
from main.tests.mixin import SignInMixin


class UserStartVerifyEmailTestCase(SignInMixin, TestCase):
    def test_success(self):
        self.web_driver.get(f"{self.live_server_url}/user/start_verify_email/")
        self.sign_in()

        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(len(self.find_elements("Sent verify email.")), 1)
        self.assertIn(
            f"{self.live_server_url}/user/verify_email?token=",
            mail.outbox[0].body,
        )
        self.assertEqual(mail.outbox[0].subject, "Verify Email")
        self.assertIn("email@email.com", mail.outbox[0].to)
