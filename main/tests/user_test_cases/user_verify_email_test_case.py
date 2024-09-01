from secrets import token_urlsafe

from django.core.cache import cache
from django.test import override_settings
from selenium.webdriver.common.by import By

from main.tests import TestCase
from main.tests.login_mixin import LoginMixin


class UserVerifyEmailTestCase(LoginMixin, TestCase):
    @override_settings(DEBUG=True)
    def test_success(self):
        token = token_urlsafe()
        cache.set("verify_email.1", token)

        self.web_driver.get(f"{self.live_server_url}/user/verify_email/?token={token}")
        self.login()
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        self.assertEqual(len(self.find_elements("Email verified: True")), 1)
