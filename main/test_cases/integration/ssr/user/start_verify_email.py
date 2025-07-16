from django.core import mail
from django.core.cache import cache
from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.test_cases.integration.ssr import SsrTestCase


class StartVerifyUserEmailSsrTestCase(SsrTestCase):
    fixtures = ["sessions", "users"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.get(reverse("user-start-verify-email"))
        self.assertRedirects(
            response,
            f"{reverse('user-sign-in')}"
            f"?{urlencode({'next': reverse('user-start-verify-email')})}",
        )

    def test_get(self) -> None:
        """Test get form."""
        self.add_session_cookie()
        response = self.client.get(reverse("user-start-verify-email"))
        xpath = """
        //form
            [@method='post']
            [//input[@type='submit']]
        """
        self.assert_match_once(fromstring(response.content), xpath)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        self.add_session_cookie()
        response = self.client.post(reverse("user-start-verify-email"))
        self.assertRedirects(response, reverse("user-read"))
        sentinel = object()
        token = cache.get("verify_user_email.1", sentinel)
        self.assertIsNot(token, sentinel)
        self.assertEqual(
            f"http://testserver{reverse('user-verify-email')}"
            f"?{urlencode({'token': token})}",
            mail.outbox[0].body,
        )
        self.assertEqual(mail.outbox[0].subject, "Verify Email")
        self.assertIn("email1@email.com", mail.outbox[0].to)
