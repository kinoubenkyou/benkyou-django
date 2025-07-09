from secrets import token_urlsafe

from django.core.cache import cache
from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.models import User
from main.test_cases.integration.ssr import SsrTestCase


class VerifyUserEmailSsrTestCase(SsrTestCase):
    fixtures = ["sessions", "users"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.get(reverse("user-verify-email"))
        self.assertRedirects(
            response,
            f"{reverse('user-sign-in')}"
            f"?{urlencode({'next': reverse('user-verify-email')})}",
        )

    def test_get(self) -> None:
        """Test get form."""
        self.add_session_cookie()
        token = token_urlsafe()
        cache.set("verify_user_email.1", token)
        response = self.client.get(
            f"{reverse('user-verify-email')}?{urlencode({'token': token})}"
        )
        xpath = f"""
        .//form
        [@method='post']
        [.//input[@name="token" and @value="{token}"]]
        [.//input[@type='submit']]
        """
        self.assertEqual(len(fromstring(response.content).xpath(xpath)), 1)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        self.add_session_cookie()
        token = token_urlsafe()
        cache.set("verify_user_email.1", token)
        response = self.client.post(
            f"{reverse('user-verify-email')}?{urlencode({'token': token})}",
            {"token": token},
        )
        self.assertRedirects(response, reverse("user-read"))
        self.assertTrue(User.objects.get(pk=1).email_is_verified)

    def test_incorrect_token(self) -> None:
        """Test incorrect token case."""
        self.add_session_cookie()
        token = token_urlsafe()
        cache.set("verify_user_email.1", token)
        response = self.client.post(
            f"{reverse('user-verify-email')}?{urlencode({'token': f'{token}_'})}",
            {"token": f"{token}_"},
        )
        self.assertEqual(
            len(fromstring(response.content).xpath(".//*[text()='incorrect token']")),  # type: ignore[no-untyped-call]
            1,
        )

    def test_token_not_found(self) -> None:
        """Test token not found case."""
        self.add_session_cookie()
        token = token_urlsafe()
        cache.set("verify_user_email.1", token, 0)
        response = self.client.post(
            f"{reverse('user-verify-email')}?{urlencode({'token': token})}",
            {"token": token},
        )
        self.assertEqual(
            len(fromstring(response.content).xpath(".//*[text()='token not found']")),  # type: ignore[no-untyped-call]
            1,
        )
