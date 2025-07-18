from secrets import token_urlsafe

from django.conf import settings
from django.core.cache import cache
from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.fixtures.session_id import SessionId
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
        self.client.cookies[settings.SESSION_COOKIE_NAME] = SessionId.SIGNED_IN
        token = token_urlsafe()
        cache.set("verify_user_email.1", token)
        response = self.client.get(
            f"{reverse('user-verify-email')}?{urlencode({'token': token})}"
        )
        xpath = f"""
        .//form
            [@method='post']
            [.//input
                [@name="token"]
                [@value="{token}"]
            ]
            [.//input[@type='submit']]
        """
        self.assert_match_once(fromstring(response.content), xpath)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        self.client.cookies[settings.SESSION_COOKIE_NAME] = SessionId.SIGNED_IN
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
        self.client.cookies[settings.SESSION_COOKIE_NAME] = SessionId.SIGNED_IN
        token = token_urlsafe()
        cache.set("verify_user_email.1", token)
        response = self.client.post(
            f"{reverse('user-verify-email')}?{urlencode({'token': f'{token}_'})}",
            {"token": f"{token}_"},
        )
        self.assert_match_once(
            fromstring(response.content),  # type: ignore[no-untyped-call]
            ".//*[text()='incorrect token']",
        )

    def test_token_not_found(self) -> None:
        """Test token not found case."""
        self.client.cookies[settings.SESSION_COOKIE_NAME] = SessionId.SIGNED_IN
        token = token_urlsafe()
        cache.set("verify_user_email.1", token, 0)
        response = self.client.post(
            f"{reverse('user-verify-email')}?{urlencode({'token': token})}",
            {"token": token},
        )
        self.assert_match_once(
            fromstring(response.content),  # type: ignore[no-untyped-call]
            ".//*[text()='token not found']",
        )
