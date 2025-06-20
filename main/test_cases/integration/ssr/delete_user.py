from django.urls import reverse
from django.utils.http import urlencode
from lxml.html import fromstring

from main.models import User
from main.test_cases.integration.ssr import SsrTestCase


class DeleteUserSsrTestCase(SsrTestCase):
    fixtures = ["sessions", "users"]

    def test_authentication_required(self) -> None:
        """Test authentication required."""
        response = self.client.get(reverse("user-delete"))
        self.assertRedirects(
            response,
            f"{reverse('user-sign-in')}?{urlencode({'next': reverse('user-delete')})}",
        )

    def test_get(self) -> None:
        """Test get form."""
        self.add_session_cookie()
        response = self.client.get(reverse("user-delete"))
        xpath = """
        //form
        [@method='post']
        [//input[@type='submit']]
        """
        self.assertEqual(len(fromstring(response.content).xpath(xpath)), 1)  # type: ignore[no-untyped-call]

    def test_post(self) -> None:
        """Test submit form."""
        self.add_session_cookie()
        response = self.client.post(reverse("user-delete"))
        self.assertRedirects(response, reverse("user-sign-in"))
        self.assertFalse(User.objects.filter(pk=1).exists())
