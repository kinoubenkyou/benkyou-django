from django.core import mail
from django.core.cache import cache
from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.test_cases.integration.ssr import SsrTestCase


class StartResetUserPasswordSsrTestCase(SsrTestCase):
    fixtures = ["user"]

    def test_get(self) -> None:
        """Test get form."""
        response = self.client.get(reverse("user-start-reset-password"))
        xpath = """
        //form
        [@method='post']
        [//input[@name='username']]
        [//input[@type='submit']]
        """
        self.assertEqual(len(fromstring(response.content).xpath(xpath)), 1)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        response = self.client.post(
            reverse("user-start-reset-password"), {"username": "username1"}
        )
        self.assertRedirects(response, reverse("user-sign-in"))
        sentinel = object()
        token = cache.get("reset_user_password.username1", sentinel)
        self.assertIsNot(token, sentinel)
        self.assertEqual(
            f"http://testserver{reverse('user-reset-password')}"
            f"?{urlencode({'token': token, 'username': 'username1'})}",
            mail.outbox[0].body,
        )
        self.assertEqual(mail.outbox[0].subject, "Reset Password")
        self.assertIn("email1@email.com", mail.outbox[0].to)

    def test_username_not_found(self) -> None:
        """Test username not found case."""
        response = self.client.post(
            reverse("user-start-reset-password"), {"username": "username1_"}
        )
        self.assertEqual(
            len(fromstring(response.content).xpath("//*[text()='username not found']")),  # type: ignore[no-untyped-call]
            1,
        )
