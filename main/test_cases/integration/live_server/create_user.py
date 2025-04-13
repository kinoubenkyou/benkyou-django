from django.core import mail
from django.core.cache import cache
from django.utils.http import urlencode
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import url_changes

from main.models import User
from main.test_cases.integration.live_server import LiveServerTestCase


class CreateUserLiveServerTestCase(LiveServerTestCase):
    def test(self) -> None:
        """Test success case."""
        url = f"{self.live_server_url}/user/create/"
        self.web_driver.get(url)
        username = "username1"
        last_name = "last_name1"
        first_name = "first_name1"
        email = "email1@email.com"
        password = "Dr0wss@p1"
        self.find_input_and_replace_value("username", username)
        self.find_input_and_replace_value("last_name", last_name)
        self.find_input_and_replace_value("first_name", first_name)
        self.find_input_and_replace_value("email", email)
        self.find_input_and_replace_value("password1", password)
        self.find_input_and_replace_value("password2", password)
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        self.web_driver_wait.until(url_changes(url))
        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}/user/sign_in/",
        )
        user = User.objects.filter(username=username).first()
        self.assertIsNotNone(user)
        self.assertEqual(user.last_name, last_name)  # type: ignore[union-attr]
        self.assertEqual(user.first_name, first_name)  # type: ignore[union-attr]
        self.assertEqual(user.email, email)  # type: ignore[union-attr]
        self.assertTrue(user.check_password(password))  # type: ignore[union-attr]
        self.assertFalse(user.email_is_verified)  # type: ignore[union-attr]
        sentinel = object()
        token = cache.get(f"verify_user_email.{user.pk}", sentinel)  # type: ignore[union-attr]
        self.assertIsNot(token, sentinel)
        self.assertEqual(
            f"{self.live_server_url}/user/verify_email?{urlencode({'token': token})}",
            mail.outbox[0].body,
        )
        self.assertEqual(mail.outbox[0].subject, "Verify Email")
        self.assertIn(email, mail.outbox[0].to)
