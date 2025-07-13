from django.urls import reverse
from lxml.html import fromstring

from main.models import User
from main.test_cases.integration.ssr import SsrTestCase


class DeleteUserSsrTestCase(SsrTestCase):
    fixtures = ["sessions", "users"]

    def test_get(self) -> None:
        """Test get form."""
        self.add_session_cookie()
        response = self.client.get(reverse("user-delete"))
        xpath = """
        .//form
            [@method='post']
            [//input[@type='submit']]
        """
        self.assert_match_once(fromstring(response.content), xpath)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        self.add_session_cookie()
        response = self.client.post(reverse("user-delete"))
        self.assertRedirects(response, reverse("user-sign-in"))
        self.assertFalse(User.objects.filter(pk=1).exists())
